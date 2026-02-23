# 5. Usage and Testing

## Test the Proxy
LiteLLM comes with a built-in terminal CLI to easily test your models without writing code. 

Keep your server running in one Terminal tab, open a **new** Terminal tab (`⌘ + T`), and choose one of the testing methods below:

### Method 1: Interactive Menu (Recommended)
Run the proxy tool to open a full interactive menu:
```bash
litellm-proxy
```
1. Type `chat` and press Enter.
2. It will ask for a **Model name**. Type your wildcard proxy route, for example `gemini/gemini-2.5-flash` or `ollama/llama3.2`, and press Enter.
3. You can now chat directly with the model to verify it works! Press `Ctrl-C` to exit back to the menu, and type `quit` to close the tool.

### Method 2: Direct Inline Chat
If you know the model name, you can skip the menu and launch straight into a chat session from your terminal:
```bash
litellm-proxy chat gemini/gemini-2.5-flash
```
*(Replace `gemini/gemini-2.5-flash` with your chosen Ollama or Gemini model).*

## Connect LightRAG to LiteLLM
To use LiteLLM as the engine for your LightRAG server, update your `LightRAG/.env` file in Zed:

```ini
LLM_BINDING=openai
LLM_BINDING_HOST=http://localhost:4000/v1
LLM_MODEL=gemini/gemini-2.5-flash 
LLM_BINDING_API_KEY=any-string-will-work
```

This tells LightRAG to send all requests to LiteLLM instead of directly to a specific provider.

**Next:** [6. Optional UI Launcher](6-optional-ui-launcher.md)
