@echo off
echo ===================================================
echo   Mode Avenue Project Setup
echo ===================================================
echo.
echo 1. Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python and try again.
    pause
    exit /b 1
)

echo.
echo 2. Rebuilding virtual environment (venv)...
if exist venv (
    echo Deleting existing venv...
    rmdir /s /q venv
)
python -m venv venv
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create virtual environment!
    pause
    exit /b 1
)

echo.
echo 3. Upgrading pip...
venv\Scripts\python -m pip install --upgrade pip

echo.
echo 4. Installing required packages from requirements.txt...
venv\Scripts\pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo 5. Testing Database Connection...
venv\Scripts\python test_db_connection.py
if %errorlevel% neq 0 (
    echo [WARNING] Database connection test failed or returned errors.
)

echo.
echo ===================================================
echo   Setup Completed Successfully!
echo ===================================================
echo.
echo To run your project:
echo 1. Open a command prompt or VS Code terminal in this folder
echo 2. Run the application using:
echo    venv\Scripts\python run.py
echo.
echo 3. Open your browser and navigate to:
echo    http://127.0.0.1:5000
echo.
echo ===================================================
pause
