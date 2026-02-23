# 3. Configuration

LiteLLM looks for a `config.yaml` file to know which models to serve and what API keys to use.

## 1. Create the Config File

1. Open Finder and go to your home folder (`⇧ + ⌘ + H`).
2. **Important:** Press `⇧ + ⌘ + .` to show hidden files. Finder will not let you create a folder starting with a dot unless hidden files are visible.
3. Create a new folder (`⇧ + ⌘ + N`) and name it `.litellm` (it will warn you about starting with a dot, confirm it).
4. Inside the `.litellm` folder, open Zed and create a new blank document.
4. Paste the configuration block (see below) into the document.
5. Save the document inside `.litellm` and name it EXACTLY `config.yaml`.

## 2. Config Template

This template sets up a cloud model (Gemini), a local model (Ollama), local/cloud embedding models (Nomic, Gemini), and a custom OpenAI-Compatible server. Copy and paste this into your `config.yaml`:

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

  # A local embedding model using Ollama
  - model_name: nomic-embed-text
    litellm_params:
      model: ollama/nomic-embed-text
      api_base: "http://localhost:11434"

  # A cloud embedding model using Gemini
  - model_name: gemini-embedding-001
    litellm_params:
      model: gemini/gemini-embedding-001
      api_key: "os.environ/GEMINI_API_KEY"

  # A cloud model using Gemini (Wildcard route for ANY Gemini model)
  - model_name: gemini/*
    litellm_params:
      model: gemini/*
      api_key: "os.environ/GEMINI_API_KEY"

  # An OpenAI-Compatible Server (e.g., vLLM, LM Studio, Together AI)
  - model_name: custom-openai-server
    litellm_params:
      model: openai/<your-model-name>
      api_base: "http://your-server-address/v1"
      api_key: "os.environ/CUSTOM_API_KEY" # Optional, if your server requires it
```

## How API Keys Work
The config uses `os.environ/...` to securely load API keys from your environment. You tell your Mac the key before starting the server.

**Next:** [4. Running the Server](4-running-the-server.md)
