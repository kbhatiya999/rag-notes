# 5. Usage and Testing

## Test the Proxy
LiteLLM comes with a built-in terminal CLI to easily test your models without writing code. 

Keep your server running in one Terminal tab, open a **new** Terminal tab (`⌘ + T`), and choose one of the testing methods below:

### Method 1: Interactive Menu (Recommended)
Run the proxy tool to open a full interactive menu:
```bash
litellm-proxy
```
1. Type `models list` and press Enter to see all available models configured in your proxy.
2. Type `chat` and press Enter.
3. It will ask for a **Model name**. Type your wildcard proxy route, for example `gemini/gemini-2.5-flash` or `ollama/llama3.2`, and press Enter.
4. You can now chat directly with the model to verify it works! Press `Ctrl-C` to exit back to the menu, and type `quit` to close the tool.

### Method 2: Direct Inline Command
If you want to view models and test them rapidly without the menu, you can run these commands straight from your terminal:

**View Available Models:**
```bash
litellm-proxy models list
```

**Launch Testing Chat:**
```bash
litellm-proxy chat gemini/gemini-2.5-flash
```
*(Replace `gemini/gemini-2.5-flash` with a model from your list).*

### Method 3: Advanced API Requests (cURL)
If you want to test specific APIs like embeddings or image/video generation, you can use raw `curl` commands against the proxy endpoint `http://localhost:4000/v1`.

**Test Embeddings:**
```bash
curl -X POST "http://localhost:4000/v1/embeddings" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-embedding-001",
    "input": "This request needs no LiteLLM key"
  }'
```

**Test Image Generation & Save to Downloads:**
Because the Gemini `images/generations` API returns a base64-encoded JSON response rather than a direct image URL, you can pipe the output through `jq` to decode and save the image directly into your `Downloads` folder.

1. **Create the output folders** first (if they don't exist):
   ```bash
   mkdir -p ~/Downloads/litellm/images ~/Downloads/litellm/videos
   ```

2. **Generate and Save Image 1 (Minimalist Logo):**
   ```bash
   curl -s -X POST "http://localhost:4000/v1/images/generations" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "gemini/imagen-4.0-fast-generate-001",
       "prompt": "A minimalist logo of a mountain",
       "size": "1024x1024"
     }' | jq -r '.data[0].b64_json' | base64 -D > ~/Downloads/litellm/images/mountain-logo.png
     
   open ~/Downloads/litellm/images/mountain-logo.png
   ```

3. **Generate and Save Image 2 (Cyberpunk Cat):**
   ```bash
   curl -s -X POST "http://localhost:4000/v1/images/generations" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "gemini/imagen-4.0-fast-generate-001",
       "prompt": "A digital painting of a neon cyberpunk cat",
       "n": 1,
       "size": "1024x1024"
     }' | jq -r '.data[0].b64_json' | base64 -D > ~/Downloads/litellm/images/cyberpunk-cat.png
     
   open ~/Downloads/litellm/images/cyberpunk-cat.png
   ```
*(Note: If you receive a "command not found: jq" error, you can install it via `brew install jq`).*

**Next:** [6. Optional UI Launcher](6-optional-ui-launcher.md)
