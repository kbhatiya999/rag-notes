# Zed Text Editor

Zed is a fast, Rust-based code editor that supports Language Server Protocol (LSP) for real-time error checking.

## Install Zed

1. Open **Terminal** (`⌘ + Space`, type "Terminal", press Enter).
2. Run these commands to install Zed and the file association tool (`duti`):
   ```bash
   brew install --cask zed
   brew install duti
   ```

## Make Zed the Default Editor

We want Zed to automatically open when double-clicking Markdown (`.md`) notes or configuration (`.yml`, `.env`) files in Finder.

1. Open **Terminal**.
2. Run these commands to configure macOS file associations:
   ```bash
   duti -s dev.zed.Zed public.plain-text all
   duti -s dev.zed.Zed public.data all
   duti -s dev.zed.Zed public.source-code all
   ```

**Note:** Do not map `public.unix-executable` to Zed! macOS uses the target application for `public.unix-executable` as the default Terminal emulator. If you configure Zed for it, Finder's built-in "Open in Terminal" service on folders will mistakenly try to open the folder inside Zed instead.

Now, any markdown, configuration, programming language, or extensionless data file you double-click in Finder will instantly open in Zed.
