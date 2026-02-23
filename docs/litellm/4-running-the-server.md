# 4. Running the Server

Since all settings and keys are saved in your config and `.zshrc` files, you only need to run one short command to start your proxy.

## Start the Server

1. Open a new **Terminal**.
2. Run this command:
   ```bash
   litellm --config ~/.litellm/config.yaml
   ```

When you see `Uvicorn running on http://0.0.0.0:4000`, your AI proxy is successfully hosting all your local and cloud models.
To stop the server at any time, press `Ctrl + C` in the Terminal.

**Next:** [5. Usage and Testing](5-usage-and-testing.md)
