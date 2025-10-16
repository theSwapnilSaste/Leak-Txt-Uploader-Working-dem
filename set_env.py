#!/usr/bin/env python3
"""
Script to set environment variables for the Telegram bot.
Run this before starting the bot to set all required environment variables.
"""

import os

# Set environment variables
# os.environ['BOT_NAME'] = 'ZENITH_BOT'
# os.environ['BOT_TOKEN'] = ''
# os.environ['API_ID'] = ''
# os.environ['API_HASH'] = ''
# os.environ['MONGO_URI'] = ''
# os.environ['OWNER_ID'] = '504848353'
# os.environ['LOG_CHANNEL_ID'] = '-1002971022913'

print("✅ Environment variables set successfully!")
print("🚀 You can now run your bot with: python modules/main.py")
print("\n📋 Configuration Summary:")
print(f"Bot Name: {os.environ['BOT_NAME']}")
print(f"API ID: {os.environ['API_ID']}")
print(f"Owner ID: {os.environ['OWNER_ID']}")
print(f"Log Channel ID: {os.environ['LOG_CHANNEL_ID']}")
print("\n⚠️  Bot Token and API Hash are set but hidden for security.")
