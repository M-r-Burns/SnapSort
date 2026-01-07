# SnapSort 📸

## 🟢 DOWNLOAD INSTRUCTIONS (Start Here!)

For non-computer people like my grandma, downloading will take 2 minutes and is super easy. Just follow the instructions below.

If you want to use the app, just follow these 3 steps. You do not need to look at any other files on this page.

*Currently works for Mac and may or may not work for Windows. It has also not been extensively tested, but it worked for my use case.*

---

### Step 1: Click the Link Below

Click this link to download the app to your computer:

👉 [**CLICK HERE TO DOWNLOAD SNAPSORT FOR MAC**](https://github.com/M-r-Burns/SnapSort/releases/download/v1.0/SnapSort.zip)

---

### Step 2: Drag to Desktop

1. Find the `SnapSort.zip` file in your **Downloads** folder  
2. Double-click it — it will turn into an app icon  
3. Drag that app to your **Desktop**

---

### Step 3: The "Right-Click" Trick (Very Important!)

⚠️ Your Mac might try to block the app because I didn't pay Apple $100.  
To fix this, you only need to do this **ONCE**:

- Do **NOT** normal-click the app  
- **Right-click** (or Control-click) the app icon  
- Click **Open** in the menu  
- A warning box will appear — click **Open**

✅ Now the app is safe! You can open it normally from now on.

---

## Why I Built This

I routinely drag photos and videos off of my iPhone into a folder on an external hard drive just to clear space. But when I actually went to clean that folder up, I realized what a nightmare it was. Constantly dragging files to the trash and waiting for previews to load one-by-one took forever.

I built SnapSort so I could just fly through my photos. You click **Next**, **Back**, **Delete**, or **Favorite**, and the app handles the rest.

One thing I did differently: if you click **Delete**, it doesn't actually wipe the photo. It creates a **"Deleted"** folder right inside your current folder and moves the photo there. That way, when you're finished, you can just dump that whole folder into the trash — or if you realize you made a mistake, you can easily pull the photo back out.

It’s all local, so there are zero privacy issues, and I made sure the setup takes under two minutes. It should be easy enough for my grandma to use. I hope this helps someone else as much as it helped me!

---

## Features

- 🚀 **Zero-Lag:** Pre-loads heavy iPhone HEIC files so you never stare at a loading screen  
- 🔒 **100% Private:** Your photos never leave your hard drive. No internet required  
- 🍎 **Mac Native:** Includes a "Reveal in Finder" button to quickly locate files  
- ⌨️ **Keyboard Friendly:** Use your mouse or fly through with number keys or arrow keys  

---

## Usage Controls

You can click the buttons on the screen, but the keyboard is much faster:

- **Left Arrow / 1:** Previous Image  
- **Right Arrow / 4:** Next Image (Keep)  
- **Backspace / 2:** Move to "Deleted" Folder  
- **Up Arrow / 3:** Move to "Favorites" Folder  

---

## For Developers

If you want to modify the code or run it via Python:

1. Clone this repository  
2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the launcher:

```bash
./LAUNCH_ME.command
```

---

## Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML5, CSS3, JavaScript (Web Workers)  
- **Packaging:** PyInstaller  

---

## License

MIT License. Feel free to use and modify!
