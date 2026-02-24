echo "Enter commit message: "
read commit_message
git add .
git commit -m "$commit_message"
git push
# uv run mkdocs gh-deploy
