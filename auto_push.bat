@echo off
echo [AUTO] Starting Full Automation Sequence...

REM 1. Check if GitHub CLI is installed
where gh >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] GitHub CLI (gh) is not installed!
    echo I cannot create the repository remotely for you automatically.
    echo.
    echo Please install it: https://cli.github.com/
    echo Or manually run:
    echo git remote add origin https://github.com/YOUR_USER/PolyglotArchitect.git
    echo git push -u origin main
    pause
    exit /b
)

REM 2. Authenticate check (basic)
echo [AUTO] Checking GitHub authentication...
gh auth status >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] You are not logged into GitHub CLI.
    echo Please run: gh auth login
    pause
    exit /b
)

REM 3. Create Repo (Public)
echo [AUTO] Creating public repository 'PolyglotArchitect' on GitHub...
gh repo create PolyglotArchitect --public --source=. --remote=origin --push

if %errorlevel% equ 0 (
    echo [SUCCESS] Repository created and pushed!
    echo View it at: https://github.com/%USERNAME%/PolyglotArchitect
    start https://github.com/%USERNAME%/PolyglotArchitect
) else (
    echo [WARNING] Repo creation likely failed (maybe it already exists?).
    echo Attempting simple push...
    git push -u origin main
)

pause
