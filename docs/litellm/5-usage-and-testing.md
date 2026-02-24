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

**Next:** [6. Optional UI Launcher](6-optional-ui-launcher.md)
