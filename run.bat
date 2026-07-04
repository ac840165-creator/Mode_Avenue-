@echo off
title Mode Avenue Web Server
echo ===================================================
echo   Starting Mode Avenue Web Server...
echo ===================================================
echo.
cd /d "%~dp0"
venv\Scripts\python.exe run.py
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to start server!
    echo Please make sure you ran setup.bat first.
    pause
)
