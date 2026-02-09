# Setup

Follow these steps to create your own notes website.

## Step 1: Open Terminal

Open the Terminal app on your computer.

## Step 2: Create a new project

Type this and press Enter:

```bash
uv init my-notes --no-package
```

This creates a new folder called `my-notes`.

## Step 3: Go into the folder

```bash
cd my-notes
```

## Step 4: Install the tools

```bash
uv add mkdocs mkdocs-material
```

This installs MkDocs (the tool that makes websites from text files).

## Step 5: Create the website structure

```bash
uv run mkdocs new .
```

This creates a `docs` folder where you'll write your notes.

## Step 6: See your website

```bash
uv run mkdocs serve --livereload
```

Open your browser and go to: `http://127.0.0.1:8000`

You'll see your website! Any changes you make will show up automatically.

## What's next?

Your website is running on your computer. To share it with others, go to **Upload to GitHub**.
