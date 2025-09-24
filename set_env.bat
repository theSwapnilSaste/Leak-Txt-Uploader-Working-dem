@echo off
REM Windows batch script to set environment variables for the Telegram bot

echo Setting environment variables...

set BOT_NAME=ZENITH_BOT
set BOT_TOKEN=7626013382:AAEvmqpHw4otevswmJbtSw7yK03rGYVmc4M
set API_ID=22746239
set API_HASH=a98ec8cfd8572a3a7c936cf828fe6215
set MONGO_URI=mongodb+srv://herukobanna:ankit999@cluster0.xs772me.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
set OWNER_ID=7792539085
set LOG_CHANNEL_ID=7792539085

echo.
echo ✅ Environment variables set successfully!
echo 🚀 You can now run your bot with: python modules/main.py
echo.
echo 📋 Configuration Summary:
echo Bot Name: %BOT_NAME%
echo API ID: %API_ID%
echo Owner ID: %OWNER_ID%
echo Log Channel ID: %LOG_CHANNEL_ID%
echo.
echo ⚠️ Bot Token and API Hash are set but hidden for security.
echo.
pause
