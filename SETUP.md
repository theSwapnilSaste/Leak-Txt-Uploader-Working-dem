# Telegram Bot Setup Guide

## Configuration Complete ✅

Your Telegram bot has been configured with the provided credentials:

### Credentials Used:
- **Bot Token**: `7626013382:AAEvmqpHw4otevswmJbtSw7yK03rGYVmc4M`
- **API ID**: `22746239`
- **API Hash**: `a98ec8cfd8572a3a7c936cf828fe6215`
- **MongoDB URI**: `mongodb+srv://herukobanna:ankit999@cluster0.xs772me.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`
- **Owner ID**: `7792539085`

## How to Run the Bot

### Option 1: Using Python Script (Recommended)
```bash
python set_env.py
python modules/main.py
```

### Option 2: Using Windows Batch File
```bash
set_env.bat
python modules/main.py
```

### Option 3: Manual Environment Setup
Set these environment variables in your system:
```bash
export BOT_NAME=ZENITH_BOT
export BOT_TOKEN=7626013382:AAEvmqpHw4otevswmJbtSw7yK03rGYVmc4M
export API_ID=22746239
export API_HASH=a98ec8cfd8572a3a7c936cf828fe6215
export MONGO_URI=mongodb+srv://herukobanna:ankit999@cluster0.xs772me.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
export OWNER_ID=7792539085
export LOG_CHANNEL_ID=7792539085
```

## What Was Changed

1. ✅ Updated `modules/config.py` to properly read environment variables
2. ✅ Updated `modules/main.py` to use config variables instead of hardcoded values
3. ✅ Set your Owner ID (`7792539085`) as the authorized user
4. ✅ Created setup scripts for easy environment configuration

## Bot Commands

The bot responds to `/zenith` command (previously `/kunal`) and includes features for:
- Video downloading from various platforms
- Batch processing from .txt files
- Watermark support
- MongoDB integration for data persistence
- Channel authorization system

## Security Note ⚠️

**Important**: The credentials are now properly configured but should be kept secure. For production deployment, use environment variables or secure credential management systems.

## Next Steps

1. Run the setup script: `python set_env.py`
2. Start the bot: `python modules/main.py`
3. Test the bot by sending `/start` to your bot on Telegram
4. Use `/zenith` to start uploading content from .txt files

Your bot is ready to use! 🚀
