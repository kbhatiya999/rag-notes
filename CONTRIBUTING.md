# AI Contributor Guidelines

This document provides instructions for AI assistants on how to add new documentation and guides to this repository. Adhere to these guidelines strictly to ensure consistency and quality.

## Core Philosophy (STRICT)

- **Personal Notes Style:** These are *not* professional tutorials. Never write introductory essays ("What You'll Achieve", "The Problem"). Just define what the tool is in one sentence and move straight to the steps.
- **Finder-First:** Default to macOS Finder and Zed for all file/folder creation and configuration editing (even for files like `.env`, giving instructions on how to show hidden files in Finder).
- **No TextEdit/Notepad:** NEVER recommend TextEdit, Notepad, or full IDEs like VSCode. **Zed** is the absolute required default editor for all `.md`, `.yml`, and `.env` files.
- **Terminal for Commands Only:** Only use Terminal for things that *require* it (e.g., `uv tool install`, `brew install`). Do not use `cwd`, `mkdir`, `touch`, or `nano`.
- **Direct, Plain English:** Step 1, Step 2, Step 3. Simple sentences. No conversational padding.

## Documentation Structure

The `docs` directory is organized into top-level sections. Each section is a directory containing guides on a specific topic.

Current sections:
- `docs/notes-site/`: Guides related to setting up the MkDocs site itself.
- `docs/lightrag-server/`: Guides for the LightRAG Server application.
- `docs/dev-tools/`: Guides for supplementary developer tools (like `zoxide`).

When adding a new guide, first determine if it belongs to an existing section. If it covers a new, distinct topic, create a new top-level directory for it (e.g., `docs/new-tool/`).

## File and Directory Conventions

- **Directory:** Each multi-page guide must reside in its own subdirectory (e.g., `docs/dev-tools/zoxide/`).
- **File Naming:** Guide pages must be prefixed with a number and a hyphen to enforce order (e.g., `1-introduction.md`, `2-installation.md`).
- **File Format:** All documentation is written in Markdown (`.md`).

## Writing Style

- **Headings:** Use `#` for the main page title and `##` for major sections.
- **Emphasis:** Use **bold** (`**text**`) for UI elements, file names, and important concepts. Use backticks (`` ` ``) for commands, variable names, and file paths.
- **No Admonitions:** Do NOT use MkDocs admonitions (e.g., `!!! tip`, `!!! note`). They were explicitly removed for simplicity. Use standard bold text like **Note:** or **Tip:** instead.
- **Code Blocks:** Use fenced code blocks with language identifiers.
- **Finder/Zed Pathing:**
  - *Do NOT write:* "Use `mkdir` and `nano` to create your `.env` file."
  - *DO write:* "Create a folder in Finder. Open **Zed** (`⌘ + N`) and save your file. (Press `⇧ + ⌘ + .` to see hidden files)."

## The Contribution Workflow

Follow this procedure to add a new guide:

1.  **Analyze the Request:** Understand the user's goal for the new guide.
2.  **Plan the Structure:**
    - Identify the appropriate parent section (e.g., `dev-tools`).
    - Create a new subdirectory for the guide topic (e.g., `docs/dev-tools/new-tool/`).
    - Break the guide down into logical, numbered Markdown files (`1-topic.md`, `2-next-topic.md`, etc.).
3.  **Create Directories and Files:** Use shell commands to create the necessary directory and empty files.
4.  **Write the Content:** Populate each file with clear, step-by-step instructions, adhering to the style guide above.
5.  **Update Navigation:** Modify the `mkdocs.yml` file to add the new guide to the `nav` section. Maintain the existing structure and indentation.
