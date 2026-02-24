# 5. Usage Guide

Keep your Terminal window open with the server running (`bash ~/LightRAG/lightrag-launcher.sh`) while completing these steps.

## Use the Web Interface
When the server is running, go to:
- **Chat Interface:** `http://127.0.0.1:8020`

## Add Documents
1. Open Finder (`⌃ + ⌥ + F`) and go to your home folder.
2. Open `LightRAG`, then open `inputs`.
3. Drag and drop PDF or TXT files into this `inputs` folder.
4. Go to `http://127.0.0.1:8020` and use the "Index" button to process the new files.

## Change Settings
1. Go to the `LightRAG` folder in Finder (`⌃ + ⌥ + F`). (Press `⇧ + ⌘ + .` if you don't see `.env`).
2. Open `.env` in [Zed](../dev-tools/zed-text-editor.md).
3. Make your changes (like switching the API key) and save.
4. Restart your server (press `Ctrl + C` in Terminal, then run the script again) to apply the changes.

**Next:** [6. Optional UI Launcher](6-optional-ui-launcher.md)
