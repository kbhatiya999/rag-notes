# 6. Troubleshooting

## Common Issues

**App Quits Immediately**
1. Open Terminal and run: `~/LightRAG/lightrag-launcher.sh` to see the error.
2. If it says `command not found`, reinstall the tool: 
   ```bash
   uv tool install "lightrag-hku[offline,observability]"
   ```
3. If it says `Address already in use`, open `~/LightRAG/.env` in Zed and change `PORT=8020` to `PORT=8030`.

**Can't see `.env` in Finder**
Files starting with a dot are hidden by default. Open the `LightRAG` folder in Finder and press `⇧ + ⌘ + .` to show them.

**Server running but browser won't connect**
Check the app's text window to see exactly what port it started on, and ensure your browser matches (e.g., `http://127.0.0.1:8020`).

## File Locations

- **The App:** `/Applications/LightRAG Server.app`
- **Settings:** `~/LightRAG/.env`
- **Data & DB:** `~/LightRAG/`
- **Documents:** `~/LightRAG/inputs/`
- **Script:** `~/LightRAG/lightrag-launcher.sh`
