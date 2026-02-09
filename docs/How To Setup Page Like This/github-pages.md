# Deploy to GitHub Pages

Turn your notes into a real website that anyone can visit. It's free!

## Step 1: Deploy your site

Run this one command:

```bash
uv run mkdocs gh-deploy
```

That's it! Wait 2-3 minutes.

## Step 2: Visit your website

Your website is now live at:

```
https://YOUR-USERNAME.github.io/my-notes/
```

Replace `YOUR-USERNAME` with your GitHub username.

## How to update your website

After making changes to your notes:

```bash
git add .
git commit -m "Updated notes"
git push
uv run mkdocs gh-deploy
```

Your website will update in a few minutes.

## Summary

You now have:

1. **A notes folder** - Write text files in the `docs` folder
2. **A backup on GitHub** - Your files are saved online
3. **A live website** - Anyone can read your notes

Just write, save, and deploy. That's all there is to it!
