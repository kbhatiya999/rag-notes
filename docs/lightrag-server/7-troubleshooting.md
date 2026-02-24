# 7. Troubleshooting

## Common Issues

**Server Quits Immediately**
1. Open Terminal and run: `bash ~/LightRAG/lightrag-launcher.sh` to see the error.
2. If it says `command not found`, reinstall the tool: 
   ```bash
   uv tool install "lightrag-hku[offline,observability]"
   ```
3. If it says `Address already in use`, open `~/LightRAG/.env` in [Zed](../dev-tools/zed-text-editor.md) and change `PORT=8020` to `PORT=8030`.

**Can't see `.env` in Finder**
Files starting with a dot are hidden by default. Open the `LightRAG` folder in Finder (`⌃ + ⌥ + F`) and press `⇧ + ⌘ + .` to show them.

Check the Terminal output to see exactly what port it started on, and ensure your browser matches (e.g., `http://127.0.0.1:8020`).

**Ollama "Not Found" (404) Error during Indexing**
This happens when LightRAG tries to use an embedding model that Ollama doesn't have.
1. Make sure you have **uncommented** an embedding block in your `.env` file.
2. If using Ollama for embeddings, open Terminal and run `ollama pull bge-m3` (or whichever model you specified).
3. Check that your `EMBEDDING_MODEL` in `.env` matches the model name in Ollama exactly.

4. Restart the server; it will now recreate the database using the new dimensions.

### How to Clear the Index (Full Reset)
If you need to start fresh or fixed a model mismatch, follow these steps to wipe the database:

**Method 1: Finder (Visual)**
1. Open your `LightRAG` folder.
2. Select all files ending in `.json`, `.graphml`, `.bin`, and `.db`.
3. Move them to **Trash**. (Do NOT delete your `.env` file or the `inputs` folder).

**Method 2: Terminal (Fast)**
Open Terminal and paste this command to nuk only the database files:
```bash
rm ~/LightRAG/*.json ~/LightRAG/*.graphml ~/LightRAG/*.bin ~/LightRAG/*.db 2>/dev/null
```

## File Locations

- **Settings:** `~/LightRAG/.env`
- **Data & DB:** `~/LightRAG/` 
  - *Note: Official docs mention a `rag_storage` folder. We point the server directly to `~/LightRAG` to keep your database files in one easy-to-find place.*
- **Documents:** `~/LightRAG/inputs/`
- **Script:** `~/LightRAG/lightrag-launcher.sh`
- **The App (Optional):** `/Applications/LightRAG Server.app`
