# Coffee Bar Connoisseur - Git Sync Script
Write-Host "🎵 Coffee Bar Connoisseur - Git Sync" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green
Write-Host ""

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "❌ Not in a Git repository. Please run:" -ForegroundColor Red
    Write-Host "   git init" -ForegroundColor Yellow
    Write-Host "   git remote add origin https://github.com/fetch247/curator.git" -ForegroundColor Yellow
    Write-Host "   git config user.name 'Your Name'" -ForegroundColor Yellow
    Write-Host "   git config user.email 'your.email@example.com'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Then run this script again." -ForegroundColor Cyan
    exit 1
}

Write-Host "📁 Adding all files to Git..." -ForegroundColor Yellow
git add .

Write-Host "💾 Committing changes..." -ForegroundColor Yellow
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "☕ Update Coffee Bar Connoisseur - $timestamp"

Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Yellow
git push origin master

Write-Host ""
Write-Host "✅ Sync complete! Your changes are now live on GitHub." -ForegroundColor Green
Write-Host "🌐 Repository: https://github.com/fetch247/curator" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
