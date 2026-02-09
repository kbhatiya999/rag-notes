# Getting Started

Create your own notes website from scratch. No experience needed.

## Step 1: Open Terminal

**On Mac:**

1. Press `Cmd + Space` to open Spotlight
2. Type `Terminal`
3. Press Enter

A black window will open. This is where you type commands.

## Step 2: Create a projects folder (optional)

If you want to keep your projects organized:

```bash
mkdir -p ~/RAGprojects
cd ~/RAGprojects
```

## Step 3: Create your project

```bash
uv init rag-notes --no-package
```

This creates a new folder called `rag-notes` with your project inside.

## Step 4: Go into that folder

```bash
cd rag-notes
```

You're now in: `~/RAGprojects/rag-notes`

## Step 5: Install the website tools

```bash
uv add mkdocs mkdocs-material
```

Wait for it to finish. This downloads the tools you need.

## Step 6: Create the docs folder

```bash
uv run mkdocs new .
```

This creates a `docs` folder. Your notes go in here.

## Step 7: Start your website

```bash
uv run mkdocs serve --livereload
```

## Step 8: See your website

1. Open your web browser (Chrome, Safari, etc.)
2. Go to: `http://127.0.0.1:8000`
3. You'll see your website!

**To stop the website:** Go back to Terminal and press `Ctrl + C`

## What's next?

Your website only works on your computer right now. To put it online so others can see it, go to **Upload to GitHub**.
