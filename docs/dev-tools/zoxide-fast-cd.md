# Zoxide Fast CD

Zoxide is a faster replacement for `cd` in the Terminal. It remembers the folders you visit most often so you can jump straight to them using just `z <foldername>`.

## Installation

### 1. Install with Homebrew
Open Terminal and run:

```bash
brew install zoxide fzf
```

### 2. Hook into ZSH
Zoxide needs to launch every time you open a Terminal. We add it to your `~/.zshrc` file.

1. Open Finder (`⌃ + ⌥ + F`) and go to your home folder (`⇧ + ⌘ + H`).
2. Press `⇧ + ⌘ + .` to show hidden files.
3. Find the `.zshrc` file and open it in [Zed](zed-text-editor.md). *(If it doesn't exist, create a new blank text document and name it `.zshrc`)*.
4. Paste this line at the very bottom of the file:
   ```bash
   # Initialize Zoxide for fast folder navigation
   eval "$(zoxide init zsh)"
   ```
5. Save the file and close Zed.
6. **Restart your Terminal** for the changes to take effect.

## Basic Usage

*(Note: The `zoxide init` script we just added to your `.zshrc` automatically creates a short command called **`z`** for you to use).*

Use `cd` normally a few times to visit your project folders so Zoxide can "learn" them. After that, you can replace `cd` with `z`.

### Jump to a Folder
Instead of `cd`, just type `z` and part of the folder name:

```bash
z rag
```
(This instantly jumps to your `/Users/myuser/RAGprojects/rag-notes` folder).

### Interactive Search
If you forgot the exact name or want to see a list of matches, we can use the **Interactive Jump** command (which uses the `fzf` tool we installed in Step 1).

1. Type **`zi`** and press **Enter**.
2. Use the arrow keys `↓` `↑` (or just type a few letters) to select the right folder.
3. Press `Enter` to jump.
