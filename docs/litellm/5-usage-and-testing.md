# 5. Usage and Testing

## Test with `curl`
To test your server, keep it running in one Terminal tab, open a **new** Terminal tab (`⌘ + T`), and run:

```bash
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-2.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Hey, how are you?"
      }
    ]
  }'
```
You should see a JSON response from the model.
*(Note: To test your local Ollama model instead, just change `"model": "gemini/gemini-2.5-flash"` to `"model": "ollama/mistral-nemo"` in the command).*

## Connect LightRAG to LiteLLM
To use LiteLLM as the engine for your LightRAG server, update your `LightRAG/.env` file in Zed:

```ini
LLM_BINDING=openai
LLM_BINDING_HOST=http://localhost:4000/v1
LLM_MODEL=gemini/gemini-2.5-flash 
LLM_BINDING_API_KEY=any-string-will-work
```

This tells LightRAG to send all requests to LiteLLM instead of directly to a specific provider.
