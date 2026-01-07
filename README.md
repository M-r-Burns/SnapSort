# SnapSort 📸

## 🟢 DOWNLOAD INSTRUCTIONS (Start Here!)

For non-computer people like my grandma, downloading will take 2 minutes and is super easy. Just follow the instructions below.

If you want to use the app, just follow these steps. You do not need to look at any other files on this page.

*Currently works for Mac and may or may not work for Windows. It has also not been extensively tested, but it worked for my use case.*

---

### Click the Link Below

Click this link to download the app to your computer:

👉 [**CLICK HERE TO DOWNLOAD SNAPSORT FOR MAC**](https://github.com/M-r-Burns/SnapSort/releases/download/v1.0/SnapSort.zip)

---

### ⚠️ HOW TO OPEN IT (READ THIS!)
Because I am an independent developer (and didn't pay Apple $100), your Mac will try to block the app to be safe. You just need to tell your Mac it's okay.

**Try Method A first. If that doesn't work, use Method B.**

#### Method A: The Right-Click Trick
1.  **Right-Click** (or Control-Click) the app icon.
2.  Click **Open** in the menu.
3.  If a box appears with an **"Open"** button, click it! You are done.

#### Method B: The Settings Fix (If Method A failed)
If Method A didn't give you an "Open" button:
1.  Click **Done** on the error box.
2.  Click the **Apple Logo ** (top left corner) → **System Settings**.
3.  Click **Privacy & Security** in the sidebar.
4.  Scroll down until you see a message about "SnapSort".
5.  Click the **"Open Anyway"** button.
6.  Enter your computer password.

**You only have to do this ONCE.** After that, you can open the app normally!

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
