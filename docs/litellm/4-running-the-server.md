# 4. Running the Server

## 1. Set API Keys
If you are using cloud providers, tell Terminal your API keys before starting the server. Open Terminal and run:

```bash
export OPENAI_API_KEY="sk-xxx"
export ANTHROPIC_API_KEY="sk-yyy"
```

**Note:** These only last until you close the window. (You can add those lines to your `~/.zshrc` file if you want them to be permanent).

## 2. Start the Server
In the same Terminal window, start the server and point it to the config file:

```bash
litellm --config ~/.litellm/config.yaml
```

When you see `Uvicorn running on http://0.0.0.0:8000`, the server is ready. 
To stop it, press `Ctrl + C`.

**Next:** [5. Usage and Testing](5-usage-and-testing.md)
