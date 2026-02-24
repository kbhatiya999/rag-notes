# 5. Usage and Testing

## Test the Proxy
LiteLLM comes with a built-in terminal CLI to easily test your models without writing code. 

Keep your server running in one Terminal tab, open a **new** Terminal tab (`⌘ + T`), and follow the tests below:

### 1. View Available Models
First, run this command to see all the loaded model routes you can test via the proxy:
```bash
curl -s http://localhost:4000/v1/models | jq
```

### 2. Test Chat (Text Generation)
Send a standard OpenAI-compatible chat completion request to verify text generation:
```bash
curl -X POST "http://localhost:4000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-2.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Hello! Are you working?"
      }
    ]
  }'
```

### 3. Test Embeddings
Test the embeddings API by sending a raw `curl` command against the proxy endpoint `http://localhost:4000/v1`.
```bash
curl -X POST "http://localhost:4000/v1/embeddings" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-embedding-001",
    "input": "This request needs no LiteLLM key"
  }'
```

### 4. Test Image Generation
Because the Gemini `images/generations` API returns a base64-encoded JSON response rather than a direct image URL, you can pipe the output through `jq` to decode and save the image directly into your `Downloads` folder.

1. **Create the output folders** first (if they don't exist):
   ```bash
   mkdir -p ~/Downloads/litellm/images ~/Downloads/litellm/videos
   ```

2. **Generate and Save an Image:**
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
*(Note: If you receive a "command not found: jq" error, you can install it via `brew install jq`).*

### 5. Test Video Generation
Video generation is an asynchronous process, so it requires a multi-step script instead of a single pipeline.

1. **Start Generation:** Send the prompt to the Veo model and save the returned `id` string into a terminal variable.
   ```bash
   video_id=$(curl -s -X POST "http://localhost:4000/v1/videos" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "gemini/veo-3.1-fast-generate-preview",
       "prompt": "A cat playing with a ball of yarn in a sunny garden"
     }' | jq -r '.id')
     
   echo "Processing Video ID: $video_id"
   ```

2. **Check Status:** Run this command to poll your proxy. Wait until the `status` string changes from `processing` to `completed`.
   ```bash
   curl -s -X GET "http://localhost:4000/v1/videos/$video_id" | jq
   ```

3. **Download Video:** Once completed, run the `/content` endpoint to download the generated MP4 file to your Mac.
   ```bash
   curl -X GET "http://localhost:4000/v1/videos/$video_id/content" \
     --output ~/Downloads/litellm/videos/cat-yarn.mp4
     
   open ~/Downloads/litellm/videos/cat-yarn.mp4
   ```

**Next:** [6. Optional UI Launcher](6-optional-ui-launcher.md)
