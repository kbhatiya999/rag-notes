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

**Embedding dimension mismatch (AssertionError)**
This happens when you change your embedding model (e.g., switching from Ollama to Gemini). LightRAG cannot mix different dimensions in the same database.
1. Open your `LightRAG` folder in Finder.
2. **Delete** all files mapping to the database (e.g., `*.json`, `*.graphml`, `*.bin`, `*.db`). 
3. **Warning:** This will delete your current index. Your original text files in `inputs/` are safe.
4. Restart the server; it will now recreate the database using the new dimensions.

## File Locations

- **Settings:** `~/LightRAG/.env`
- **Data & DB:** `~/LightRAG/`
- **Documents:** `~/LightRAG/inputs/`
- **Script:** `~/LightRAG/lightrag-launcher.sh`
- **The App (Optional):** `/Applications/LightRAG Server.app`
