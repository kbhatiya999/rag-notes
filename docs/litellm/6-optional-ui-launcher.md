# 6. Optional UI Launcher

If you prefer not to use the Terminal every time you need your AI proxy, we can use a free tool called **Platypus** to wrap our launch command into a simple, double-clickable Mac app.

## Create the Launcher Script

First, we need a simple script for Platypus to run. 

1. Open Finder (`⌃ + ⌥ + F`), press `⇧ + ⌘ + H` to go home, then open your `.litellm` folder.
2. Open Zed, create a new blank document, and paste this code:
   ```bash
   #!/bin/bash
   source ~/.zshrc
   ~/.local/bin/litellm --config ~/.litellm/config.yaml
   ```
3. Save it into your `.litellm` folder as `litellm-launcher.sh`.

We need to make it executable. Open Terminal and run:
   ```bash
   chmod +x ~/.litellm/litellm-launcher.sh
   ```

## Create the App

1. Open **Platypus** from your Applications folder.
2. Fill out the settings exactly like this:
   - **App Name:** `LiteLLM Proxy`
   - **Script Path:** Click "Select...", press `⇧ + ⌘ + G` (Go to Folder), type `~/.litellm`, and select your `litellm-launcher.sh` file.
   - **Interface:** Change to **Text Window**.
   - **Identifier:** `com.litellm.proxy.app`
   - **At the very bottom**, make sure `Run script in background` and `Remain running after script exits` are both **UNCHECKED**.
3. Click **Create App** at the bottom.
4. Save it into your **Applications** folder.

## How to Use It

- **Start:** Double-click `LiteLLM Proxy.app` in your Applications folder. A text window will appear showing the server logs.
- **Stop:** Click the app's text window to bring it into focus, and press `⌘ + Q` on your keyboard to gracefully shut down the proxy.
