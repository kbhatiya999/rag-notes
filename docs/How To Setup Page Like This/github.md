# Upload to GitHub

## Commit Your Changes

First, commit all your local changes:

```bash
git add .
git commit -m "Initial commit: setup rag-notes repo with MkDocs and Material theme"
```

## Create GitHub Repository

Create a remote repository on GitHub and push your code using `gh` (GitHub CLI):

```bash
gh repo create rag-notes --source=. --remote=origin --push --public
```

Replace `--public` with `--private` if you want a private repository.

This will:
- Create a new repository on GitHub
- Connect your local repo to this remote (origin)
- Push all your local commits to GitHub

## Verify Connection

```bash
git remote -v
```

You should see your GitHub repo URL listed.

Your repo is now live at: `https://github.com/<your-username>/rag-notes`

## Push Future Changes

After making changes locally:

```bash
git add .
git commit -m "Your commit message"
git push
```

Or as a shorthand:

```bash
git add . && git commit -m "Your message" && git push
```
