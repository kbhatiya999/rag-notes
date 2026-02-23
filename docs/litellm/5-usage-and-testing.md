# 5. Usage and Testing

## Test with Interactive Proxy Menu
The easiest way to test your server is by using LiteLLM's built in interactive terminal UI. 

Keep your server running in one Terminal tab, open a **new** Terminal tab (`⌘ + T`), and run:

```bash
litellm-proxy
```

When the interactive menu opens:
1. Type `chat` and press Enter to start the interactive chat module.
2. It will ask for a **Model name**. Type your wildcard proxy route, for example `gemini/gemini-2.5-flash` or `ollama/llama3.2`, and press Enter.
3. You can now chat directly with the model to verify it works! Press `Ctrl-C` to exit back to the menu, and type `quit` to close the tool.

## Connect LightRAG to LiteLLM
To use LiteLLM as the engine for your LightRAG server, update your `LightRAG/.env` file in Zed:

```ini
LLM_BINDING=openai
LLM_BINDING_HOST=http://localhost:4000/v1
LLM_MODEL=gemini/gemini-2.5-flash 
LLM_BINDING_API_KEY=any-string-will-work
```

This tells LightRAG to send all requests to LiteLLM instead of directly to a specific provider.
