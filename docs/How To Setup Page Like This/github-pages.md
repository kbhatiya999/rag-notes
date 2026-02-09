# Deploy to GitHub Pages

Deploy your site:

```bash
uv run mkdocs gh-deploy
```

This builds your site and uploads it to GitHub. Wait 2-3 minutes.

Your site is live at: `https://YOUR-USERNAME.github.io/rag-notes/`

To update after changes:

```bash
git add . && git commit -m "Update" && git push && uv run mkdocs gh-deploy
```
