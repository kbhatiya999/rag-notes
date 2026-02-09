# Upload to GitHub

Save and upload your project:

```bash
git add .
git commit -m "Initial commit"
gh repo create rag-notes --source=. --remote=origin --push --public
```

For future changes:

```bash
git add . && git commit -m "Update" && git push
```

Next: [Deploy to GitHub Pages](github-pages.md)
