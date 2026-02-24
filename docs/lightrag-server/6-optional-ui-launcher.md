# 6. Optional UI Launcher

If you prefer not to use the Terminal every time you want to search your notes, we can use a free tool called **Platypus** to wrap our launch script into a simple, double-clickable Mac app.

## Create the App

1. Open **Platypus** from your Applications folder.
2. Fill out the settings exactly like this:
   - **App Name:** `LightRAG Server`
   - **Script Path:** Click "Select...", press `⇧ + ⌘ + G` (Go to Folder), type `~/LightRAG`, and select `lightrag-launcher.sh`.
   - **Interface:** Change to **Text Window**.
   - **At the very bottom**, make sure you **UNCHECK** these two options:
     - **Remain running after execution:** *Keep unchecked.* If enabled, the app window stays open forever even if your server script crashes, forcing you to manually kill a "zombie" process.
     - **Run in background:** *Keep unchecked.* If enabled, the app hides itself from your macOS Dock and hides its log window, making it impossible to see errors or gracefully quit the server using `⌘ + Q`.
3. Click **Create App** at the bottom.
4. Save it into your **Applications** folder.

## How to Use It

- **Start:** Open your Applications folder in Finder (`⌃ + ⌥ + F`) and double-click `LightRAG Server.app`. A small text window will appear showing the server output.
- **Stop:** Click the app's text window to bring it into focus, and press `⌘ + Q` on your keyboard. This gracefully shuts down the server. *(This is why we had to uncheck 'Run in background'—without the window, you have no easy way to press `⌘ + Q` to kill the server).*

**Next:** [7. Troubleshooting](7-troubleshooting.md)
