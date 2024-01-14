@echo off
echo Installing requirements...
pip install openai python-dotenv

if not exist .env (
    echo.
    echo Please create a .env file with your OPENAI_API_KEY before running!
    echo Example: OPENAI_API_KEY=sk-...
    echo.
    pause
    exit /b
)

echo Starting Generator...
python main.py

echo.
echo Running Validation...
python tests/validator.py

echo.
echo Generating Dashboard...
python dashboard_generator.py

pause
