# Zed Text Editor

Zed is a fast, Rust-based code editor that supports Language Server Protocol (LSP) for real-time error checking.

## Install Zed

1. Open **Terminal** (`⌘ + Space`, type "Terminal", press Enter).
2. Run this command:
   ```bash
   brew install --cask zed
   ```

## Make Zed the Default Editor

We want Zed to automatically open when double-clicking Markdown (`.md`) notes or configuration (`.yml`, `.env`) files in Finder.

1. Open **Terminal**.
2. Run these commands to configure macOS file associations:
   ```bash
   duti -s dev.zed.Zed public.plain-text all
   duti -s dev.zed.Zed public.unix-executable all
   duti -s dev.zed.Zed public.data all
   ```

Now, any plain text, markdown, configuration, or extensionless data file you double-click in Finder will instantly open in Zed.
