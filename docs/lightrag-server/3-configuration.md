# 3. Server Configuration

## 1. Create Folders
1. Open Finder (`⌃ + ⌥ + F`) and go to your home folder (`⇧ + ⌘ + H`).
2. Create a folder named `LightRAG`.
3. Open `LightRAG` and create a folder inside it named `inputs`.

## 2. Create the Configuration File
1. Open [Zed](../dev-tools/zed-text-editor.md) and create a new blank document (`⌘ + N`).
2. Paste the configuration block below into it (choose your provider section).
3. Save the file directly into the `LightRAG` folder. 
   **Note**: You must name the file EXACTLY `.env` (it will warn you that starting with a dot makes it hidden — click "Use .").

If the `.env` file disappears after saving, press `⇧ + ⌘ + .` inside Finder to show hidden files.

> [!IMPORTANT]
> **Switching Models?** If you are changing your embedding model (e.g., from Ollama to Gemini), you must delete any existing database files in your `LightRAG` folder (like `*.json` or `*.graphml`) before starting the server. LightRAG cannot mix different model dimensions.

For advanced customization beyond the basics below, refer to the official [LightRAG env.example](https://github.com/HKUDS/LightRAG/blob/main/env.example).

### The Config Template

```ini
# --- General Server Settings ---
HOST=127.0.0.1
PORT=8020
WEBUI_TITLE=My Personal RAG
WEBUI_DESCRIPTION=A private RAG system powered by LightRAG

# --- Directory Settings (Optional) ---
# LightRAG defaults to these paths if left commented out:
# WORKING_DIR=/Users/YOUR_MAC_USERNAME/LightRAG
# INPUT_DIR=/Users/YOUR_MAC_USERNAME/LightRAG/inputs

> [!NOTE]
> **Where is `rag_storage`?** The official LightRAG default is to create a folder called `rag_storage`. However, our launcher script explicitly sets the `WORKING_DIR` to your `~/LightRAG` folder directly. This puts all database files in the root of that folder for easier access.

# --- Indexing Performance ---
MAX_ASYNC=4
MAX_PARALLEL_INSERT=2
CHUNK_SIZE=1200
CHUNK_OVERLAP_SIZE=100

# ==========================================
# CHOOSE ONE PROVIDER BELOW
# ==========================================

# --- Option 1: LITELLM PROXY (Recommended) ---
# Use this for both LLM and Embeddings via your local LiteLLM Gateway
LLM_BINDING=openai
LLM_BINDING_HOST=http://localhost:4000/v1
LLM_MODEL=gemini/gemini-2.0-flash
LLM_BINDING_API_KEY=any-string-will-work

EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=http://localhost:4000/v1
EMBEDDING_MODEL=gemini/text-embedding-004
EMBEDDING_DIM=768
EMBEDDING_BINDING_API_KEY=any-string-will-work

# --- Option 2: OLLAMA ---
# LLM_BINDING=ollama
# LLM_BINDING_HOST=http://localhost:11434
# LLM_MODEL=mistral-nemo:latest
# OLLAMA_LLM_NUM_CTX=32768
# EMBEDDING_BINDING=ollama
# EMBEDDING_BINDING_HOST=http://localhost:11434
# EMBEDDING_MODEL=bge-m3:latest
# EMBEDDING_DIM=1024

# --- Option 3: OPENAI ---
# LLM_BINDING=openai
# LLM_BINDING_HOST=https://api.openai.com/v1
# LLM_MODEL=gpt-4o
# LLM_BINDING_API_KEY=sk-your-api-key-here

# --- OpenAI (Embedding) ---
# EMBEDDING_BINDING=openai
# EMBEDDING_MODEL=text-embedding-3-large
# EMBEDDING_DIM=3072
# EMBEDDING_SEND_DIM=false
# EMBEDDING_TOKEN_LIMIT=8192
# EMBEDDING_BINDING_HOST=https://api.openai.com/v1
# EMBEDDING_BINDING_API_KEY=sk-your-api-key-here

# --- Option 4: GEMINI ---
# LLM_BINDING=gemini
# LLM_MODEL=gemini-2.0-flash
# LLM_BINDING_HOST=https://generativelanguage.googleapis.com
# LLM_BINDING_API_KEY=your-gemini-api-key-here
# EMBEDDING_BINDING=gemini
# EMBEDDING_MODEL=gemini-embedding-001
# EMBEDDING_BINDING_HOST=https://generativelanguage.googleapis.com
# EMBEDDING_BINDING_API_KEY=your-gemini-api-key-here
# EMBEDDING_DIM=1536
```


**Next:** [4. Running the Server](4-running-the-server.md)
