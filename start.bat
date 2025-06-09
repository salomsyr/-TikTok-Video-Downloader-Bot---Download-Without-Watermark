@echo off
set BOT_NAME=TikTok Downloader
title %BOT_NAME% - Download TikTok Videos
:start
cls
echo ===================================
echo    TikTok Video Downloader Bot
echo ===================================
echo.

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.7 or later and try again.
    pause
    exit /b 1
)

:: Check if requirements are installed
if not exist "venv" (
    echo Setting up virtual environment...
    python -m venv venv
    call venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

:: Run the bot
python tiktok_bot.py

:: If the bot crashes, restart it
echo.
echo Bot stopped. Restarting in 5 seconds...
timeout /t 5 >nul
goto start
