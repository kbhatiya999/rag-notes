# 5. Usage Guide

## Start and Stop the Server
- **Start:** Open your Applications folder in Finder and double-click `LightRAG Server.app`.
- **Stop:** Click the app's text window and press `⌘ + Q`.

## Use the Web Interface
When the app is running, go to:
- **Chat Interface:** `http://127.0.0.1:8020`

## Add Documents
1. Open Finder and go to your home folder.
2. Open `LightRAG`, then open `inputs`.
3. Drag and drop PDF or TXT files into this `inputs` folder.
4. Go to `http://127.0.0.1:8020` and use the "Index" button to process the new files.

## Change Settings
1. Go to the `LightRAG` folder in Finder. (Press `⇧ + ⌘ + .` if you don't see `.env`).
2. Open `.env` in Zed.
3. Make your changes (like switching the API key) and save.
4. Restart the `LightRAG Server.app` to apply the changes.

**Next:** [6. Troubleshooting](6-troubleshooting.md)
