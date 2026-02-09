# Getting Started

Open Terminal (`Cmd + Space`, type `Terminal`, press Enter).

Run these commands:

```bash
mkdir -p ~/RAGprojects && cd ~/RAGprojects
uv init rag-notes --no-package
cd rag-notes
uv add mkdocs mkdocs-material
uv run mkdocs new .
uv run mkdocs serve --livereload
```

Open browser: `http://127.0.0.1:8000`

Stop server: `Ctrl + C`

Next: **Upload to GitHub**
