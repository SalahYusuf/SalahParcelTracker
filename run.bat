@echo off
cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel%==0 (set PY=python) else (set PY=py)

if not exist .venv\Scripts\python.exe (
    echo Creating private environment...
    %PY% -m venv .venv
    if errorlevel 1 (
        echo Could not create the environment. Install Python from python.org and tick "Add Python to PATH".
        pause
        exit /b 1
    )
)

echo Installing requirements...
.venv\Scripts\python.exe -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo Install failed. Check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo Open http://127.0.0.1:5000/customer in your browser
echo Press Ctrl+C to stop.
echo.
.venv\Scripts\python.exe app.py
pause
