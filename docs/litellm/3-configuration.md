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

This template sets up a cloud model (OpenAI) and a local model (Ollama). Copy and paste this into your `config.yaml`:

```yaml
# ~/.litellm/config.yaml

litellm_settings:
  drop_params: True

model_list:
  # A cloud model using OpenAI
  - model_name: gpt-4o 
    litellm_params:
      model: gpt-4o 
      api_key: "os.environ/OPENAI_API_KEY" 

  # A local model using Ollama
  - model_name: ollama/mistral-nemo 
    litellm_params:
      model: ollama/mistral-nemo 
      api_base: "http://localhost:11434" 

  # A cloud model using Claude
  - model_name: claude-3-5-sonnet
    litellm_params:
      model: claude-3-5-sonnet-20240620
      api_key: "os.environ/ANTHROPIC_API_KEY"
```

## How API Keys Work
The config uses `os.environ/...` to securely load API keys from your environment. You tell your Mac the key before starting the server.

**Next:** [4. Running the Server](4-running-the-server.md)
