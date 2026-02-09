# Deploy to GitHub Pages

Host your docs for free using GitHub Pages.

## Deploy Your Site

Make sure your `mkdocs.yml` includes:

```yaml
site_url: https://<your-username>.github.io/rag-notes/
repo_url: https://github.com/<your-username>/rag-notes
repo_name: rag-notes
```

Then deploy:

```bash
uv run mkdocs gh-deploy
```

This builds your site and pushes it to the `gh-pages` branch on GitHub.

## Access Your Live Site

Your docs are now live at:

```
https://<your-username>.github.io/rag-notes/
```

**Note:** The first deployment may take a few minutes. Refresh the link after 2-3 minutes.

## Update After Changes

After making changes and pushing to GitHub:

```bash
git add .
git commit -m "Update docs"
git push
uv run mkdocs gh-deploy
```

Or combine into one command:

```bash
git add . && git commit -m "Update docs" && git push && uv run mkdocs gh-deploy
```

## How It Works

- `mkdocs gh-deploy` builds your site and creates a `gh-pages` branch
- GitHub Pages serves content from this branch automatically
- Keep your source code on `main`, site is on `gh-pages`
