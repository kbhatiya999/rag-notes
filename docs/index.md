# My Notes

This site contains personal notes for setting up development tools, documentation sites, and local AI servers.

## Guide Directory

- **[Developer Tools](dev-tools/zoxide-fast-cd.md)**: Setting up Zoxide, [Zed](dev-tools/zed-text-editor.md), and Mac Terminal shortcuts.
- **[Notes Site Setup](notes-site/1-initial-setup.md)**: Building and publishing this documentation site.
- **[LiteLLM Server](litellm/1-what-is-litellm.md)**: Running an OpenAI-compatible proxy for local and cloud AI models. 
- **[LightRAG Server](lightrag-server/1-introduction.md)**: Running a personal RAG search server as a native Mac app.

## Finder & Global Shortcuts

> **Mac Keyboard Symbols:**
> - `⌃` = Control
> - `⌥` = Option (Alt)
> - `⇧` = Shift
> - `⌘` = Command
>
> **The Terminal "Brain" (.zshrc):**
> `.zshrc` is a special system file in your home folder that stores your API keys and custom settings. See the **[navigation guide](dev-tools/mac-terminal-shortcuts.md#5-the-terminal-brain-zshrc)** to find it.
>
> **Hidden "Dot" Folders:**
> If a folder starts with a dot (like **`.litellm`**), it is a hidden configuration folder. You must press **`⇧ + ⌘ + .`** in Finder to see it. Always include the dot when naming these folders.

Because these guides rely heavily on the macOS Finder rather than complex Terminal commands, here are the most important keyboard shortcuts to remember:

- **Launch Terminal Anywhere:** Press `⌃ + ⌥ + T` (requires [one-time setup](dev-tools/mac-terminal-shortcuts.md#1-global-terminal-shortcut)).
- **Launch Finder Anywhere:** Press `⌃ + ⌥ + F` (requires [one-time setup](dev-tools/mac-terminal-shortcuts.md#2-global-finder-shortcut)).
- **Open Terminal at Folder:** Select a folder and press `⌘ + G` (requires [one-time setup](dev-tools/mac-terminal-shortcuts.md#3-open-terminal-at-folder)).
- **Go to Parent Folder:** Press `⌘ + ↑` to go up one level.
- **Go to Folder:** Press `⇧ + ⌘ + G` in Finder to jump to a specific path.
- **Show Path Bar:** Press `⌥ + ⌘ + P` in Finder to see the folder path, which is required to Right-Click -> **Open in Terminal**.
- **Show Hidden Files:** Press `⇧ + ⌘ + .` to toggle visibility of files like `.env`.
- **Delete File:** Press `⌘ + Delete` to move a file to the Trash.
