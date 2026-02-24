# 3. Server Configuration

## 1. Create Folders
1. Open Finder and go to your home folder (`⇧ + ⌘ + H`).
2. Create a folder named `LightRAG`.
3. Open `LightRAG` and create a folder inside it named `inputs`.

## 2. Create the Configuration File
1. Open Zed and create a new blank document (`⌘ + N`).
2. Paste the configuration block below into it (choose your provider section).
3. Save the file directly into the `LightRAG` folder. 
   **Note**: You must name the file EXACTLY `.env` (it will warn you that starting with a dot makes it hidden — click "Use .").

If the `.env` file disappears after saving, press `⇧ + ⌘ + .` inside Finder to show hidden files.

### The Config Template

```ini
# --- General Server Settings ---
HOST=127.0.0.1
PORT=8020
WEBUI_TITLE=My Personal RAG
WEBUI_DESCRIPTION=A private RAG system powered by LightRAG

# --- Directory Settings ---
WORKING_DIR=/Users/YOUR_MAC_USERNAME/LightRAG
INPUT_DIR=/Users/YOUR_MAC_USERNAME/LightRAG/inputs

# --- Indexing Performance ---
MAX_ASYNC=4
MAX_PARALLEL_INSERT=2
CHUNK_SIZE=1200
CHUNK_OVERLAP_SIZE=100

# ==========================================
# CHOOSE ONE PROVIDER BELOW AND UNCOMMENT IT
# ==========================================

# --- Option 1: OLLAMA ---
# LLM_BINDING=ollama
# LLM_BINDING_HOST=http://localhost:11434
# LLM_MODEL=mistral-nemo:latest
# OLLAMA_LLM_NUM_CTX=32768
# EMBEDDING_BINDING=ollama
# EMBEDDING_BINDING_HOST=http://localhost:11434
# EMBEDDING_MODEL=bge-m3:latest
# EMBEDDING_DIM=1024

# --- Option 2: OPENAI ---
# LLM_BINDING=openai
# LLM_BINDING_HOST=https://api.openai.com/v1
# LLM_MODEL=gpt-4o
# LLM_BINDING_API_KEY=sk-your-api-key-here
# EMBEDDING_BINDING=openai
# EMBEDDING_BINDING_HOST=https://api.openai.com/v1
# EMBEDDING_MODEL=text-embedding-3-large
# EMBEDDING_BINDING_API_KEY=sk-your-api-key-here

# --- Option 3: GEMINI ---
# LLM_BINDING=gemini
# LLM_MODEL=gemini-2.5-flash
# LLM_BINDING_HOST=https://generativelanguage.googleapis.com
# LLM_BINDING_API_KEY=your-gemini-api-key-here
# EMBEDDING_BINDING=gemini
# EMBEDDING_MODEL=gemini-embedding-001
# EMBEDDING_BINDING_HOST=https://generativelanguage.googleapis.com
# EMBEDDING_BINDING_API_KEY=your-gemini-api-key-here
# EMBEDDING_DIM=1536

# --- Option 4: LITELLM PROXY ---
# LLM_BINDING=openai
# LLM_BINDING_HOST=http://localhost:4000/v1
# LLM_MODEL=gemini/gemini-2.5-flash
# LLM_BINDING_API_KEY=any-string-will-work
# (Note: You still need to uncomment an EMBEDDING block from above)
```

## 3. Create the Launcher Script
Platypus needs a simple script to launch the server.

1. Open Zed and create a new blank document (`⌘ + N`).
2. Paste this exact code:

```bash
#!/bin/zsh
export PATH="$HOME/.local/bin:$PATH"
WORKING_DIR="$HOME/LightRAG"
mkdir -p "$WORKING_DIR"
cd "$WORKING_DIR"
exec lightrag-server --working-dir "$WORKING_DIR"
```

3. Save it into your `LightRAG` folder and name it `lightrag-launcher.sh`.
4. **Make it runnable**: Open Terminal and run:
   ```bash
   chmod +x ~/LightRAG/lightrag-launcher.sh
   ```

**Next:** [4. Running the Server](4-running-the-server.md)
