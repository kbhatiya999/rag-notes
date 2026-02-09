# Setup

## Initial Project Setup

Initialize the project with `uv`:

```bash
uv init rag-notes --no-package
```

Navigate into the project:

```bash
cd rag-notes
```

Now you're in: `~/RAGprojects/rag-notes`

Add MkDocs dependencies:

```bash
uv add mkdocs mkdocs-material
```

Initialize the MkDocs structure:

```bash
uv run mkdocs new .
```

## Theme Configuration (mkdocs.yml)

Your project's appearance is controlled by `mkdocs.yml`:

```yaml
site_name: RAG Notes
site_url: https://kbhatiya999.github.io/rag-notes/
repo_url: https://github.com/kbhatiya999/rag-notes
repo_name: rag-notes

theme:
  name: material
  palette:
    # Palette toggle for light mode
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Palette toggle for dark mode
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

After editing `mkdocs.yml`, restart `uv run mkdocs serve --livereload` to see changes.

## Running Locally

Start the documentation server with live reload:

```bash
uv run mkdocs serve --livereload
```

Visit `http://127.0.0.1:8000` to preview your docs.
