# Upload to GitHub

GitHub is a website that stores your files online for free. We'll put your notes there.

## Step 1: Save your work

First, save all your files:

```bash
git add .
```

Then create a save point (called a "commit"):

```bash
git commit -m "My first save"
```

## Step 2: Create a GitHub repository

This command does everything for you - creates a place on GitHub and uploads your files:

```bash
gh repo create my-notes --source=. --remote=origin --push --public
```

**Want it private?** Change `--public` to `--private`

## Step 3: Check it worked

```bash
git remote -v
```

You should see a GitHub URL. Your files are now on GitHub!

## How to save future changes

Whenever you update your notes, run these commands:

```bash
git add .
git commit -m "Updated my notes"
git push
```

That's it! Your changes are saved online.

## What's next?

Your files are on GitHub. Now let's make them into a live website - go to **Deploy to GitHub Pages**.
