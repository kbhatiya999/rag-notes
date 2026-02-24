# Mac Terminal Shortcuts

This guide configures two highly useful custom keyboard shortcuts on macOS to drastically speed up your workflow without needing third-party tools.

## 1. Global Terminal Shortcut

This creates a true global hotkey (e.g., `⌃ + ⌥ + T`) that will instantly launch Terminal from anywhere, absolutely no matter what app you are currently in.

1. Open the macOS **Shortcuts** app.
2. Click the **+** button at the top to create a new shortcut.
3. In the search bar on the right, search for **"Open App"** and double-click it to add it to your shortcut.
4. Click the faded "App" variable in the action block and select **Terminal**.
5. Give your shortcut a name at the top (like "Launch Terminal").
6. Click the **Info (i)** button in the top right corner.
7. Click **Add Keyboard Shortcut**, then press the key combination you want to use globally (e.g., `⌃ + ⌥ + T`).

Your shortcut is now active from anywhere!

---

## 2. Global Finder Shortcut

If you want a global hotkey to bring up Finder from absolutely anywhere (just like we did for Terminal in Step 1):

1. Open the macOS **Shortcuts** app.
2. Click the **+** button at the top to create a new shortcut.
3. In the search bar on the right, search for **"Open App"** and double-click it.
4. Click the faded "App" variable in the action block and select **Finder**.
5. Give your shortcut a name at the top (like "Launch Finder").
6. Click the **Info (i)** button in the top right corner.
7. Click **Add Keyboard Shortcut**, then press the key combination you want to use globally (e.g., `⌃ + ⌥ + F`).

---

## 3. Open Terminal at Folder

This configures a shortcut (`⌘ + G`) to instantly open a Terminal window directly inside whichever folder you currently have selected in Finder.

### Enable the Service
1. Open macOS **System Settings**.
2. Go to **Keyboard** on the left menu.
3. Click the **Keyboard Shortcuts...** button on the right.
4. Select **Services** on the left menu.
5. Expand the **Files and Folders** section.
6. Check the box next to **New Terminal at Folder**.

### Set the Shortcut
1. In that same window, double-click the word "none" (or the existing shortcut) on the right side of the **New Terminal at Folder** row.
2. Press **`⌘ + G`** on your keyboard to record the new shortcut.
3. Click **Done**.

Now, when you select any folder in Finder, you can press `⌘ + G` to instantly open a Terminal window at that exact location.

---

## 4. Open Finder from Terminal

If you are already working in the Terminal and want to visually see your files, you don't need a keyboard shortcut. You can instantly open your current Terminal directory in a new Finder window by simply typing:

```bash
open .
```
*(Note: The `.` represents your current directory).*
