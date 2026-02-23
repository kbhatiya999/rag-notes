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
*(Note: To test a local Ollama model instead, change `"model": "gemini/gemini-2.5-flash"` to `"model": "ollama/mistral-nemo"` or any other downloaded Ollama model).*

## Test Embeddings
You can also test the local `nomic-embed-text` model:

```bash
curl http://localhost:4000/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-004",
    "input": ["Hello world"]
  }'
```
*(Note: To test your local Ollama embeddings instead, change `"model": "text-embedding-004"` to `"model": "nomic-embed-text"`).*

## Connect LightRAG to LiteLLM
To use LiteLLM as the engine for your LightRAG server, update your `LightRAG/.env` file in Zed:

```ini
LLM_BINDING=openai
LLM_BINDING_HOST=http://localhost:4000/v1
LLM_MODEL=gemini/gemini-2.5-flash 
LLM_BINDING_API_KEY=any-string-will-work
EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=http://localhost:4000/v1
EMBEDDING_MODEL=text-embedding-004
```

This tells LightRAG to send all generation and embedding requests to LiteLLM.
