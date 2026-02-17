# LightRAG Server Setup Guide

Turn LightRAG into a native Mac app that you can double-click to run.

## What You'll Get

A Mac application that runs a local RAG (Retrieval Augmented Generation) server. Double-click to start, works with Ollama or OpenAI.

## Before You Start

You need these installed first:
- **Ollama** (for local AI) OR **OpenAI API key** (for cloud AI)
- **Platypus** app - Download from [sveinbjorn.org/platypus](https://sveinbjorn.org/platypus)

## Step 1: Install LightRAG

**➜ TERMINAL:** Open Terminal (press `⌘+Space`, type "Terminal", press Enter)

**➜ TERMINAL:** Copy and paste this command, then press Enter:

```bash
uv tool install "lightrag-hku[offline,observability]"
```

Wait for it to finish (takes 1-2 minutes). You'll see "Installed 103 packages" when done.

**➜ TERMINAL:** Verify it worked by typing:

```bash
which lightrag-server
```

You should see: `/Users/yourusername/.local/bin/lightrag-server`

## Step 2: Create Folders

**➜ FINDER:** Open Finder (click the Finder icon in your dock)

**➜ FINDER:** Press `⌘+Shift+H` to go to your Home folder

**➜ FINDER:** Press `⌘+Shift+N` to create a new folder, name it `LightRAG`

**➜ FINDER:** Create another new folder (same way), name it `inputs`

You now have:
- `~/LightRAG/` - where the server stores data
- `~/inputs/` - where you put documents to index

## Step 3: Create Launcher Script

**➜ TERMINAL:** Copy and paste this entire block, then press Enter:

```bash
cat > ~/LightRAG/lightrag-launcher.sh << 'EOF'
#!/bin/zsh
#
# LightRAG Server Launcher
# Wrapper script for use with Platypus.app
#

# Ensure local bin is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Data directory
WORKING_DIR="$HOME/LightRAG"

# Create data directory if it doesn't exist
mkdir -p "$WORKING_DIR"

# Change to working directory so .env file is found
cd "$WORKING_DIR"

echo "Starting LightRAG Server..."
echo "  Config: $WORKING_DIR/.env"
echo "  Data:   $WORKING_DIR"
echo ""
echo "Loading configuration from .env file..."
echo "Press Ctrl+C to stop the server"
echo "----------------------------------------"

# Let .env file control all settings
exec lightrag-server --working-dir "$WORKING_DIR"
EOF
```

**➜ TERMINAL:** Make it executable by typing:

```bash
chmod +x ~/LightRAG/lightrag-launcher.sh
```

## Step 4: Create Configuration File

**➜ FINDER:**
- Press `⌘+Shift+H` to go Home
- Open the `LightRAG` folder
- Right-click in empty space → **"New File"**
- Name it: `.env` (starts with a dot)

**➜ TEXTEDIT:** Open the `.env` file in TextEdit (or VS Code/Cursor):
- Right-click `.env` → **"Open With"** → **"TextEdit"**

**➜ TEXTEDIT:** Copy ONE of the options below into your `.env` file and save.

---

### General Settings (use for all options)

```
HOST=127.0.0.1
PORT=8020
WEBUI_TITLE=My LightRAG
WEBUI_DESCRIPTION=Personal RAG System

WORKING_DIR=/Users/yourusername/LightRAG
INPUT_DIR=/Users/yourusername/LightRAG/inputs

MAX_ASYNC=4
MAX_PARALLEL_INSERT=2
CHUNK_SIZE=1200
CHUNK_OVERLAP_SIZE=100
```

!!! note "Replace `yourusername` with your actual Mac username"
    To find your username, open Terminal and type `whoami`

---

### Option 1: Ollama (Free, Local)

Add to your `.env`:

```
LLM_BINDING=ollama
LLM_BINDING_HOST=http://localhost:11434
LLM_MODEL=mistral-nemo:latest
OLLAMA_LLM_NUM_CTX=32768

EMBEDDING_BINDING=ollama
EMBEDDING_BINDING_HOST=http://localhost:11434
EMBEDDING_MODEL=bge-m3:latest
EMBEDDING_DIM=1024
```

---

### Option 2: OpenAI

Add to your `.env`:

```
LLM_BINDING=openai
LLM_BINDING_HOST=https://api.openai.com/v1
LLM_MODEL=gpt-4o
LLM_BINDING_API_KEY=sk-your-api-key-here

EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=https://api.openai.com/v1
EMBEDDING_MODEL=text-embedding-3-large
EMBEDDING_BINDING_API_KEY=sk-your-api-key-here
```

---

### Option 3: Google Gemini

Add to your `.env`:

```
LLM_BINDING=gemini
LLM_MODEL=gemini-2.5-flash
LLM_BINDING_HOST=https://generativelanguage.googleapis.com
LLM_BINDING_API_KEY=your-gemini-api-key-here

EMBEDDING_BINDING=gemini
EMBEDDING_MODEL=gemini-embedding-001
EMBEDDING_BINDING_HOST=https://generativelanguage.googleapis.com
EMBEDDING_BINDING_API_KEY=your-gemini-api-key-here
EMBEDDING_DIM=1536
```

---

### Option 4: Anthropic Claude (via OpenAI-compatible API)

Add to your `.env`:

```
LLM_BINDING=openai
LLM_BINDING_HOST=https://api.anthropic.com/v1
LLM_MODEL=claude-3-5-sonnet-20241022
LLM_BINDING_API_KEY=your-anthropic-api-key-here

EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=https://api.openai.com/v1
EMBEDDING_MODEL=text-embedding-3-large
EMBEDDING_BINDING_API_KEY=your-openai-api-key-here
```

---

### Option 5: LiteLLM Proxy (Any Model)

Use this if you have LiteLLM Proxy running locally on port 8000. Supports any LLM provider.

Add to your `.env`:

```
LLM_BINDING=openai
LLM_BINDING_HOST=http://localhost:8000/v1
LLM_MODEL=your-model-name-here
LLM_BINDING_API_KEY=any-key-or-sk-test

EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=http://localhost:8000/v1
EMBEDDING_MODEL=embedding-model-name
EMBEDDING_BINDING_API_KEY=any-key-or-sk-test
```

---

**➜ TEXTEDIT:** After pasting, press `⌘+S` to save

## Step 5: Test It Works

**➜ TERMINAL:** Type this and press Enter:

```bash
~/LightRAG/lightrag-launcher.sh
```

**What you should see:**
```
Starting LightRAG Server...
  Config: /Users/yourusername/LightRAG/.env
  Data:   /Users/yourusername/LightRAG

Loading configuration from .env file...
...
INFO: Uvicorn running on http://127.0.0.1:8020 (Press CTRL+C to quit)
```

**➜ BROWSER:** Open your web browser and go to: `http://127.0.0.1:8020`

You should see the LightRAG web interface!

**➜ TERMINAL:** Press `Ctrl+C` to stop the server (hold Control and press C)

## Step 6: Create the Mac App with Platypus

**➜ FINDER:** Open your Applications folder:
- Press `⌘+Shift+A` in Finder
- Find and double-click **Platypus**

**➜ PLATYPUS:** Fill in these fields:

1. **Script Path:**
   - Click the **"Select..."** button
   - Press `⌘+Shift+H` to go to your Home folder
   - Open the `LightRAG` folder
   - Click on `lightrag-launcher.sh`
   - Click **"Open"**

2. **App Name:**
   - Type: `LightRAG Server`

3. **Interface:**
   - Click the dropdown menu
   - Select **"Text Window"**

4. **Identifier:**
   - Type: `com.lightrag.server`

5. **Checkboxes at bottom:**
   - Make sure BOTH boxes are **UNCHECKED** (no checkmarks)
   - "Strip Nib" - leave unchecked
   - "Create symlink" - leave unchecked

**➜ PLATYPUS:** Click the big **"Create App"** button at the bottom

**➜ SAVE DIALOG:**
- Navigate to **Applications** (press `⌘+Shift+A`)
- Click **"Create"**

Done! You now have a LightRAG Server app in your Applications folder.

## Step 7: Using Your New App

### Starting the Server

**➜ FINDER:**
- Press `⌘+Shift+A` to open Applications
- Double-click **LightRAG Server**

A window will open showing the server starting up.

### Opening the Web Interface

**➜ BROWSER:** Open your browser and go to:
```
http://127.0.0.1:8020
```

You can also access:
- **API Documentation**: `http://127.0.0.1:8020/docs`

### Adding Documents

**➜ FINDER:**
- Press `⌘+Shift+H` to go Home
- Open the `LightRAG` folder
- Open the `inputs` folder inside it
- Drag and drop your PDF or text files here

**➜ BROWSER:** Use the web interface to index these documents

!!! note "Document folder location"
    Documents go in `~/LightRAG/inputs/` — this is set by `INPUT_DIR` in your `.env` file

### Stopping the Server

**➜ APP WINDOW:**
- Click on the LightRAG Server window
- Press `⌘+Q` to quit

OR press `Ctrl+C` in the window

## Changing Settings

All settings are in one file: `~/LightRAG/.env`

### How to Edit Settings

**➜ FINDER:**
- Press `⌘+Shift+H` to go Home
- Open the `LightRAG` folder
- Right-click on `.env` file (you may need to press `⌘+Shift+.` to see hidden files)
- Choose **"Open With"** → **"TextEdit"**

**➜ TEXTEDIT:**
- Change any settings you want
- Press `⌘+S` to save
- Close TextEdit

**➜ RESTART:** Quit and restart the LightRAG Server app to apply changes


## Troubleshooting

### App won't start or shows errors

**➜ TERMINAL:** Test the script directly to see the error:

```bash
~/LightRAG/lightrag-launcher.sh
```

Read the error message. Common issues:

**"No module named 'ollama'":**

**➜ TERMINAL:** Reinstall with all dependencies:
```bash
uv tool install "lightrag-hku[offline,observability]"
```

**"Port already in use":**

**➜ TEXTEDIT:** Open `~/LightRAG/.env` and change:
```
PORT=8020
```
to a different number like:
```
PORT=9000
```

### Can't see .env file in Finder

**➜ FINDER:**
- Go to the LightRAG folder
- Press `⌘+Shift+.` (Command+Shift+Period)
- Hidden files like `.env` will now appear

### Server starts but browser shows "Can't connect"

1. Make sure the server is actually running (check the app window)
2. Check what port it's using in the server output
3. Go to `http://127.0.0.1:PORT` (replace PORT with the actual number)

## Where Everything Lives

For reference, here's where all the files are:

| What | Where |
|------|-------|
| **Your Mac App** | `/Applications/LightRAG Server.app` |
| **Settings file** | `~/LightRAG/.env` |
| **Data storage** | `~/LightRAG/` folder |
| **Documents to index** | `~/inputs/` folder |
| **Script file** | `~/LightRAG/lightrag-launcher.sh` |

## Quick Reference

| Action | How |
|--------|-----|
| **Start server** | Double-click LightRAG Server in Applications |
| **Stop server** | Press `⌘+Q` or `Ctrl+C` in app window |
| **Web interface** | http://127.0.0.1:8020 |
| **Change settings** | Edit `~/LightRAG/.env`, then restart app |
| **Add documents** | Drop files into `~/LightRAG/inputs/` |

## Need More Help?

- **API Documentation:** http://127.0.0.1:8020/docs (when server is running)
- **LightRAG GitHub:** https://github.com/HKUDS/LightRAG
- **Platypus:** https://sveinbjorn.org/platypus
