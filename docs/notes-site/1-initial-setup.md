# 1. Initial Setup

These are the notes for setting up this documentation site from scratch on a Mac. 

## Prerequisites

You need two things installed on your Mac. Open the Terminal app (`⌘ + Space`, type Terminal) and run these two commands one after the other:

1. **Homebrew**: 
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **uv**: 
## Setup the Project

1. **Create the Folders (in Finder)**: 
   Open Finder and go to your home folder (`⇧ + ⌘ + H`). 
   Create a new folder named `RAGprojects`. 
   Open that folder, and create another new folder inside it named `rag-notes`.

2. **Install MkDocs (in Terminal)**:
   In your new `rag-notes` folder in Finder, look at the very top menu bar and click **View** > **Show Path Bar** (or press `⌥ + ⌘ + P`). 
   You will see the folder path at the bottom of the Finder window. **Right-click** the `rag-notes` folder in that path and select **Open in Terminal**. 
   
   In the Terminal window that pops up, copy and paste this whole block:
   ```bash
   uv init --no-package
   uv add mkdocs mkdocs-material
   uv run mkdocs new .
   ```

3. **Configure the Site**:
   Go back to the `rag-notes` folder in Finder. You will see a file named `mkdocs.yml` that was just created.
   Double-click `mkdocs.yml` to open it in Zed. 
   Delete everything in the file, and paste this simple configuration instead:

   ```yaml
   site_name: My Notes
   theme: 
     name: material
     features:
       - content.code.copy
   
   markdown_extensions:
     - pymdownx.highlight:
         anchor_linenums: true
     - pymdownx.superfences
     - pymdownx.snippets

   nav:
     - Home: index.md
   ```
   Save the file and close Zed.

## Run the Site

Whenever you want to view your notes locally on your Mac:
1. Open the `rag-notes` folder in Finder.
2. In the Path Bar at the bottom of the Finder window, **Right-click** `rag-notes` and select **Open in Terminal**.
3. Run the included script:

```bash
bash run_dev.sh
```

Then open your browser and go to `http://127.0.0.1:8000`.

**Next:** [2. Writing Content](2-writing-content.md)
