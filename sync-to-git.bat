@echo off
echo 🎵 Coffee Bar Connoisseur - Git Sync
echo ======================================
echo.

REM Check if we're in a git repository
if not exist ".git" (
    echo ❌ Not in a Git repository. Please run:
    echo    git init
    echo    git remote add origin https://github.com/fetch247/curator.git
    echo    git config user.name "Your Name"
    echo    git config user.email "your.email@example.com"
    echo.
    echo Then run this script again.
    pause
    exit /b 1
)

echo 📁 Adding all files to Git...
git add .

echo 💾 Committing changes...
git commit -m "☕ Update Coffee Bar Connoisseur - %date% %time%"

echo 🚀 Pushing to GitHub...
git push origin master

echo.
echo ✅ Sync complete! Your changes are now live on GitHub.
echo 🌐 Repository: https://github.com/fetch247/curator
echo.
pause