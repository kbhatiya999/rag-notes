# 2. Writing Content

All your notes are just written in plain text files inside the `docs/` folder, using Markdown format.

## Add a New Page

1. **Create a file (in Finder)**:
   Open the `RAGprojects/rag-notes/docs` folder in Finder. 
   Open Zed, create a new blank document (`⌘ + N`), and save it into that `docs` folder. 
   Name it something like `my-new-note.md` (make sure it ends in `.md`, not `.txt`).

2. **Write in Markdown**:
   In your new file, write your notes. Use `#` for headers, `*` for italics, `**` for bold, and `-` for bullet points.
   ```markdown
   # My Note
   This is a **bold** word.
   - Point 1
   - Point 2

   ```python
   # Code blocks automatically get a copy button!
   print("Hello World")
   ```
   ```

3. **Add to the Menu**:
   For the page to show up on the website's sidebar, you have to attach it to the navigation menu. 
   Open your `mkdocs.yml` file in Zed. 
   Under `nav:`, add the exact name of your new file:
   ```yaml
   nav:
     - Home: index.md
     - My New Note: my-new-note.md
   ```

Save the files. If the `run_dev.sh` server is currently running, your browser will update automatically.

## Organize in Folders

If you want to group notes together into sections:
1. Open the `docs/` folder in Finder.
2. Create a new folder inside it (e.g., name it `tutorials`).
3. Save your `.md` files into that new folder.
4. Open `mkdocs.yml` in Zed. List the folder name as a section, and indent the files underneath it:
   ```yaml
   nav:
     - Home: index.md
     - Tutorials:
       - Guide 1: tutorials/guide-1.md
       - Guide 2: tutorials/guide-2.md
   ```

**Next:** [3. Publishing Site](3-publishing-site.md)
