# 4. Running the Server

To start your Personal Search Server, you just need to run the launch script from your Terminal.

## Start the Server

1. Open **Terminal**.
2. Run this command:
   ```bash
   cd ~/LightRAG && lightrag-server
   ```
3. Wait a few seconds until you see `Uvicorn running on http://127.0.0.1:8020`.

The server is now running in the background of that Terminal window. Do not close the window while you want to use the search.

## Test It

1. Open your browser.
2. Go to `http://127.0.0.1:8020`.
3. You should see the LightRAG chat interface load successfully.

## Stop the Server

When you are done using LightRAG:
1. Go back to the Terminal window running the server.
2. Press `Ctrl + C` on your keyboard to shut it down.

**Next:** [5. Usage Guide](5-usage.md)
