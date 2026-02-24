# 3. Publishing Site

You can back up your notes to GitHub and host them on GitHub Pages for free. 

## Requirements
* You need a GitHub account.
* You need Git installed. (If you aren't sure, don't worry—the Mac will automatically prompt you to install it if you try to run a git command without it).
* Install the GitHub CLI: Open Terminal and run `brew install gh`

## 1. Initial Upload

If you are uploading this project for the first time, you need to use Terminal to send the files to GitHub.

1. Open your `rag-notes` folder in Finder (`⌃ + ⌥ + F`).
2. In the Path Bar at the bottom of the window, **Right-click** `rag-notes` and select **Open in Terminal**. *(If you don't see the Path Bar, click View > Show Path Bar in the top menu)*.
3. In the Terminal window that opens, run these commands one after the other:

```bash
git init
git add .
git commit -m "Initial commit"
gh repo create rag-notes --source=. --remote=origin --push --public
```
*(Note: If `gh` asks you to log in, just follow the prompts to open your browser and authenticate).*

## 2. Publish to GitHub Pages

Once everything is uploaded, tell MkDocs to build the site and deploy it. In the same Terminal window, run:

```bash
uv run mkdocs gh-deploy
```

Your site will be live in a few minutes at `https://<YOUR-GITHUB-USERNAME>.github.io/rag-notes/`.

## 3. How to Update Later

Whenever you add new notes or make changes in Finder, you need to save and re-publish your site:

1. Open **Finder** (`⌃ + ⌥ + F`), right-click the `rag-notes` folder in the bottom Path Bar, and select **Open in Terminal**.
2. Run these commands:

```bash
git add .
git commit -m "update notes"
git push
uv run mkdocs gh-deploy
```
