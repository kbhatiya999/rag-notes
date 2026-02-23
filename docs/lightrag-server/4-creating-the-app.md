# 4. Creating the Mac App

We will use Platypus to wrap the terminal script into a double-clickable Mac app.

## 1. Test the Script First

Before making the app, make sure your config works:

1. Open Terminal and run: `~/LightRAG/lightrag-launcher.sh`
2. Wait until you see `Uvicorn running on http://127.0.0.1:8020`
3. Go to `http://127.0.0.1:8020` in your browser to verify it loads.
4. Press `Ctrl + C` in Terminal to stop the server.

## 2. Create the App with Platypus

1. Open **Platypus** from your Applications folder.
2. Fill out the settings exactly like this:
   - **App Name:** `LightRAG Server`
   - **Script Path:** Click "Select...", press `⇧ + ⌘ + G`, type `~/LightRAG`, and select `lightrag-launcher.sh`.
   - **Interface:** Change to **Text Window**.
   - **Identifier:** `com.lightrag.server.app`
   - **At the very bottom**, make sure `Run script in background` and `Remain running after script exits` are both **UNCHECKED**.
3. Click **Create App** at the bottom.
4. Save it into your **Applications** folder.

You now have a clickable `LightRAG Server.app` in your Applications folder!

**Next:** [5. Usage Guide](5-usage.md)
