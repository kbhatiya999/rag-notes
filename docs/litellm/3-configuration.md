# 3. Configuration

LiteLLM looks for a `config.yaml` file to know which models to serve and what API keys to use.

## 1. Create the Config File

1. Open Finder (`⌃ + ⌥ + F`) and go to your home folder (`⇧ + ⌘ + H`).
2. **Important:** Press `⇧ + ⌘ + .` to show hidden files. Finder will not let you create a folder starting with a dot unless hidden files are visible.
3. Create a new folder (`⇧ + ⌘ + N`) and name it `.litellm` (it will warn you about starting with a dot, confirm it).
4. Inside the `.litellm` folder, open [Zed](../dev-tools/zed-text-editor.md) and create a new blank document.
4. Paste the configuration block (see below) into the document.
5. Save the document inside `.litellm` and name it EXACTLY `config.yaml`.

## 2. Config Template

This template sets up a cloud model (Gemini) and a local model (Ollama). Copy and paste this into your `config.yaml`:

```yaml
# ~/.litellm/config.yaml

litellm_settings:
  drop_params: True

model_list:
  # A local model using Ollama (Wildcard route for ANY Ollama model)
  - model_name: ollama/*
    litellm_params:
      model: ollama/*
      api_base: "http://localhost:11434" 

  # A cloud model using Gemini (Wildcard route for ANY Gemini model)
  - model_name: gemini/*
    litellm_params:
      model: gemini/*
      api_key: "os.environ/GEMINI_API_KEY"
```

## 3. Set Your API Key
The config file searches your Mac's environment for the `GEMINI_API_KEY`. We need to save it to your Terminal profile so it's always available.

**Important:** The `.zshrc` file is located in your **Home Folder** (`⇧ + ⌘ + H`), NOT inside `.litellm` or `LightRAG`.

1. Open Finder (`⌃ + ⌥ + F`) and go to your home folder (`⇧ + ⌘ + H`).
2. Press `⇧ + ⌘ + .` to show hidden files.
3. Open `.zshrc` in [Zed](../dev-tools/zed-text-editor.md).
4. Add this line to the bottom, replacing `your-key-here` with your actual Google AI Studio API key:
   ```bash
   export GEMINI_API_KEY="your-key-here"
   ```
5. Save the file and close Zed.

**Next:** [4. Running the Server](4-running-the-server.md)
