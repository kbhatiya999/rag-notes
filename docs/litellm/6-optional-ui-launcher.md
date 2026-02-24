# 6. Optional UI Launcher

If you prefer not to use the Terminal every time you need your AI proxy, we can use a free tool called **Platypus** to wrap our launch command into a simple, double-clickable Mac app.

## Create the Launcher Script

First, we need a simple script for Platypus to run. 

1. Open Finder (`⌃ + ⌥ + F`), press `⇧ + ⌘ + H` to go home, then open your `.litellm` folder.
2. Open [Zed](../dev-tools/zed-text-editor.md), create a new blank document, and paste this code:
   *(Note: macOS GUI apps don't load your Terminal environment by default. We must explicitly export the Homebrew paths so it can find your installed tools.)*
   ```bash
   #!/bin/bash
   export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
   source ~/.zshrc
   ~/.local/bin/litellm --config ~/.litellm/config.yaml
   ```
3. Save it into your `.litellm` folder as `litellm-launcher.sh`.

4. **Make it Executable:** While still in the `.litellm` folder in Finder, press `⌥ + ⌘ + P` to show the Path Bar at the bottom of the window. **Right-click** `.litellm` in that Path Bar and select **Open in Terminal**. Then run:
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
   - **At the very bottom**, make sure **Remain running after execution** is **CHECKED** (this keeps the log window open so you can see the reason if the server crashes) and **Run in background** is **UNCHECKED**.
3. Click **Create App** at the bottom.
4. Save it into your **Applications** folder.

## How to Use It

- **Start:** Double-click `LiteLLM Proxy.app` in your Applications folder. A text window will appear showing the server logs.
- **Stop:** Click the app's text window to bring it into focus, and press `⌘ + Q` on your keyboard to gracefully shut down the proxy.
