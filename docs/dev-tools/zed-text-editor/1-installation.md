# 1. Installation

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
   duti -s dev.zed.Zed .md all
   duti -s dev.zed.Zed .yml all
   duti -s dev.zed.Zed .yaml all
   duti -s dev.zed.Zed .env all
   duti -s dev.zed.Zed .txt all
   ```

Now, any `.md`, `.yml`, `.yaml`, `.env`, or `.txt` file you double-click in Finder will instantly open in Zed.

**Next:** You can now proceed to [Setup Notes Site](../../notes-site/1-initial-setup.md).
