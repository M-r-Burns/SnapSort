import os
import sys
import webbrowser
import threading
import time
import datetime
import shutil
import io
import subprocess 
from flask import Flask, render_template, request, jsonify, send_from_directory, send_file

# --- RESOURCE PATH ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- HEIC SETUP ---
try:
    from PIL import Image
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

app = Flask(__name__, template_folder=resource_path('templates'))
target_folder = ""
last_heartbeat = time.time()

ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov', '.webp', '.heic', '.avi'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    global last_heartbeat
    last_heartbeat = time.time()
    return jsonify({"status": "alive"})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """Immediate kill switch"""
    os._exit(0)

# --- FOLDER PICKER ---
@app.route('/select_folder_native', methods=['POST'])
def select_folder_native():
    global target_folder
    try:
        cmd = """osascript -e 'POSIX path of (choose folder with prompt "Select Folder to Sort")'"""
        output = subprocess.check_output(cmd, shell=True)
        path = output.decode('utf-8').strip()

        if path:
            target_folder = path
            # RETURNS PATH SO FRONTEND CAN DISPLAY IT
            return jsonify({"status": "success", "path": path})
        else:
            return jsonify({"status": "cancel"}) 
            
    except subprocess.CalledProcessError:
        return jsonify({"status": "cancel"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# --- NEW: REVEAL IN FINDER ---
@app.route('/reveal', methods=['POST'])
def reveal_file():
    filename = request.json.get('filename')
    try:
        full_path = os.path.join(target_folder, filename)
        if os.path.exists(full_path):
            # macOS command to reveal file in Finder
            subprocess.call(['open', '-R', full_path]) 
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "error", "message": "File not found"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# --- HELPER TO GET CURRENT FOLDER INFO ---
@app.route('/get_folder_info')
def get_folder_info():
    if target_folder:
        return jsonify({"path": target_folder, "name": os.path.basename(target_folder)})
    return jsonify({"path": "", "name": ""})

@app.route('/set_folder', methods=['POST'])
def set_folder():
    global target_folder
    path = request.json.get('path')
    if path:
        path = path.strip().strip('"').strip("'")
        if os.path.exists(path) and os.path.isdir(path):
            target_folder = path
            return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Folder not found"})

def is_valid(filename):
    return os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS and not filename.startswith('.')

def get_readable_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024: return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} TB"

@app.route('/files')
def list_files():
    if not target_folder: return jsonify([])
    sort_method = request.args.get('sort', 'date_asc')
    file_list = []
    try:
        with os.scandir(target_folder) as entries:
            for entry in entries:
                if entry.is_file() and is_valid(entry.name):
                    stats = entry.stat()
                    dt_object = datetime.datetime.fromtimestamp(stats.st_mtime)
                    file_list.append({
                        "name": entry.name,
                        "path": entry.path,
                        "timestamp": stats.st_mtime,
                        "date_str": dt_object.strftime("%B %d, %Y %I:%M %p"),
                        "size": get_readable_size(stats.st_size),
                        "type": "video" if entry.name.lower().endswith(('.mp4', '.mov', '.avi')) else "image"
                    })
        
        if sort_method == 'date_desc': file_list.sort(key=lambda x: x['timestamp'], reverse=True)
        elif sort_method == 'name': file_list.sort(key=lambda x: x['name'])
        else: file_list.sort(key=lambda x: x['timestamp'])
        
        return jsonify(file_list)
    except Exception as e:
        print(f"Error scanning: {e}")
        return jsonify([])

@app.route('/file/<path:filename>')
def serve_file(filename):
    full_path = os.path.join(target_folder, filename)
    ext = os.path.splitext(filename)[1].lower()

    if ext in ['.heic', '.heif']:
        try:
            img = Image.open(full_path)
            img_io = io.BytesIO()
            img.convert('RGB').save(img_io, 'JPEG', quality=85)
            img_io.seek(0)
            return send_file(img_io, mimetype='image/jpeg')
        except Exception as e:
            return send_from_directory(target_folder, filename)
    
    return send_from_directory(target_folder, filename)

@app.route('/delete', methods=['POST'])
def delete_file():
    filename = request.json.get('filename')
    try:
        delete_dir = os.path.join(target_folder, "Deleted")
        os.makedirs(delete_dir, exist_ok=True)
        shutil.move(os.path.join(target_folder, filename), os.path.join(delete_dir, filename))
        return jsonify({"status": "moved"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

@app.route('/favorite', methods=['POST'])
def favorite_file():
    filename = request.json.get('filename')
    try:
        fav_dir = os.path.join(target_folder, "Favorites")
        os.makedirs(fav_dir, exist_ok=True)
        shutil.move(os.path.join(target_folder, filename), os.path.join(fav_dir, filename))
        return jsonify({"status": "moved"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5001")

def monitor_shutdown():
    time.sleep(3) 
    while True:
        time.sleep(1)
        if time.time() - last_heartbeat > 3: 
            os._exit(0)

if __name__ == '__main__':
    monitor_thread = threading.Thread(target=monitor_shutdown, daemon=True)
    monitor_thread.start()
    threading.Timer(1, open_browser).start()
    app.run(port=5001)
