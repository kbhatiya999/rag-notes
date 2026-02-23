# 2. Installation

## 1. Install with Homebrew
Open Terminal and run:

```bash
brew install zoxide
```

## 2. Hook into ZSH
Zoxide needs to launch every time you open a Terminal. We add it to your `~/.zshrc` file.

1. Open Finder and go to your home folder (`⇧ + ⌘ + H`).
2. Press `⇧ + ⌘ + .` to show hidden files.
3. Find the `.zshrc` file and open it in **Zed**. *(If it doesn't exist, create a new blank text document and name it `.zshrc`)*.
4. Paste this line at the very bottom of the file:
   ```bash
   # Initialize Zoxide for fast folder navigation
   eval "$(zoxide init zsh)"
   ```
5. Save the file and close Zed.
6. **Restart your Terminal** for the changes to take effect.

**Next:** [3. Basic Usage](3-basic-usage.md)
