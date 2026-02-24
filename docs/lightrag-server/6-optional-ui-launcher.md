# 6. Optional UI Launcher

If you prefer not to use the Terminal every time you want to search your notes, we can use a free tool called **Platypus** to wrap our launch script into a simple, double-clickable Mac app.

## Create the App

1. Open **Platypus** from your Applications folder.
2. Fill out the settings exactly like this:
   - **App Name:** `LightRAG Server`
   - **Script Path:** Click "Select...", press `⇧ + ⌘ + G` (Go to Folder), type `~/LightRAG`, and select `lightrag-launcher.sh`.
   - **Interface:** Change to **Text Window**.
   - **Identifier:** `com.lightrag.server.app`
   - **At the very bottom**, make sure **Remain running after execution** and **Run in background** are both **UNCHECKED** (this ensures the app displays its log window and correctly shuts down the server when you quit it).
3. Click **Create App** at the bottom.
4. Save it into your **Applications** folder.

## How to Use It

- **Start:** Open your Applications folder in Finder (`⌃ + ⌥ + F`) and double-click `LightRAG Server.app`. A small text window will appear showing the server output.
- **Stop:** Click the app's text window to bring it into focus, and press `⌘ + Q` on your keyboard to gracefully shut down the server.

**Next:** [7. Troubleshooting](7-troubleshooting.md)
