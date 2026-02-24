# 5. Usage and Testing

## Test the Proxy
LiteLLM comes with a built-in terminal CLI to easily test your models without writing code. 

Keep your server running in one Terminal tab, open a **new** Terminal tab (`⌘ + T`), and follow the tests below:

### 1. View Available Models
First, run this command to see all the loaded model routes you can test via the proxy:
```bash
curl -s http://localhost:4000/v1/models | jq '.data |= if length > 3 then .[0:3] + [{"id": "... (\(length - 3) more models hidden)", "object": "model"}] else . end'
```

**Example Output:**
```json
{
  "object": "list",
  "data": [
    {
      "id": "gemini/*",
      "object": "model",
      "created": 1677610602,
      "owned_by": "openai"
    },
    {
      "id": "ollama/*",
      "object": "model",
      "created": 1677610602,
      "owned_by": "openai"
    },
    {
      "id": "gemini/gemini-1.5-flash-8b-exp-0924",
      "object": "model",
      "created": 1677610602,
      "owned_by": "openai"
    },
    {
      "id": "... (42 more models hidden)",
      "object": "model"
    }
  ]
}
```

### 2. Test Chat (Text Generation)
Send a standard OpenAI-compatible chat completion request to verify text generation:
```bash
curl -s -X POST "http://localhost:4000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-2.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Hello! Are you working?"
      }
    ]
  }' | jq
```

**Example Output:**
```json
{
  "id": "s2edaYjLMKbJ4-EPp-KL6AQ",
  "created": 1771923379,
  "model": "gemini/gemini-2.5-flash",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! That's a good question...\n\nAs an AI, I don't \"work\" in the human sense (like having shifts or needing breaks). However, I am always active and ready to process information and assist you.\n\nSo, yes, you could say I'm always \"working\" or rather, always available!\n\nHow can I help you today?",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 778,
    "prompt_tokens": 7,
    "total_tokens": 785
  }
}
```

### 3. Test Embeddings
Test the embeddings API by sending a raw `curl` command against the proxy endpoint. Because embedding models return massive arrays (e.g., 3072 raw numbers), this command uses a custom `jq` filter to keep your terminal clean:
```bash
curl -s -X POST "http://localhost:4000/v1/embeddings" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-embedding-001",
    "input": "This request needs no LiteLLM key"
  }' | jq '.data[0].embedding |= [.[0], .[1], .[2], "...", "(\(. | length) items)"]'
```

**Example Output:**
```json
{
  "model": "gemini/gemini-embedding-001",
  "data": [
    {
      "embedding": [
        -0.015254181,
        0.018891979,
        0.0023873092,
        "...",
        "(3072 items)"
      ],
      "index": 0,
      "object": "embedding"
    }
  ],
  "object": "list",
  "usage": {
    "completion_tokens": 0,
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}
```

**How the `jq` filter works:**
* `|=`: The update operator replaces the value of `.data[0].embedding` with the array defined on the right.
* `.[0], .[1], .[2]`: Extracts only the first three float values.
* `"..."`: Appends a literal ellipsis string.
* `\(. | length)`: Pipes the original, full embedding array (`.`) to the `length` function, calculates the total count (e.g., 3072), and dynamically injects the number into the final string.

### 4. Test Image Generation
Because the Gemini `images/generations` API returns a base64-encoded JSON response rather than a direct image URL, you must decode the payload to see the image.

1. **Create the output folders** first (if they don't exist):
   ```bash
   mkdir -p ~/Downloads/litellm/images ~/Downloads/litellm/videos
   ```

2. **Generate Multiple Images:** Run this command to generate 2 images and save the raw API JSON response into a variable. 
   ```bash
   response=$(curl -s -X POST "http://localhost:4000/v1/images/generations" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "gemini/imagen-4.0-fast-generate-001",
       "prompt": "A minimalist logo of a mountain",
       "size": "1024x1024",
       "n": 2
     }')
   ```
   
3. **Decode and Open Images:** Run this loop. It searches the JSON array, decodes every embedded base64 string into a unique PNG file, and opens each one side-by-side.
   ```bash
   count=1
   echo "$response" | jq -r '.data[].b64_json' | while read -r b64; do
     output_path=~/Downloads/litellm/images/mountain-logo-$count.png
     echo "$b64" | base64 -D > "$output_path"
     open "$output_path"
     ((count++))
   done
   ```
   
4. **View Clean JSON Metrics:** Finally, print the structure of the JSON response to your terminal. This filter hides the massive base64 strings so you can easily review your token usage and execution metadata.
   ```bash
   echo "$response" | jq '.data[].b64_json = ["...", "(base64 image data hidden)"]'
   ```

   **Example Output:**
   ```json
   {
     "created": 1771923595,
     "data": [
       {
         "b64_json": [
           "...",
           "(base64 image data hidden)"
         ],
         "revised_prompt": null,
         "url": null
       },
       {
         "b64_json": [
           "...",
           "(base64 image data hidden)"
         ],
         "revised_prompt": null,
         "url": null
       }
     ],
     "usage": {
       "total_tokens": 0,
       "input_tokens": 0,
       "output_tokens": 0
     }
   }
   ```

   **Generated Asset:**

   ![Generated Mountain Logo](assets/mountain-logo.png)

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

   **Example Output:**
   ```json
   {
     "id": "video_bGl0ZWxs...",
     "object": "video",
     "status": "processing",
     "created_at": null,
     "completed_at": null,
     "error": null
   }
   ```

3. **Download Video:** Once completed, wait a few moments for the video to fully finalize on the servers, then run the `/content` endpoint to download the generated MP4 file to your Mac.
   ```bash
   sleep 20
   curl -s -X GET "http://localhost:4000/v1/videos/$video_id/content" \
     --output ~/Downloads/litellm/videos/cat-yarn.mp4
     
   open ~/Downloads/litellm/videos/cat-yarn.mp4
   ```

   **Generated Asset:**

   <video controls src="../assets/cat-yarn.mp4" width="100%"></video>

**Next:** [6. Optional UI Launcher](6-optional-ui-launcher.md)
