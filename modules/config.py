# config.py
import os

# Bot Configuration
BOT_NAME = os.environ.get('BOT_NAME', 'NANA_LTUW_BOT')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
MONGO_URI = os.environ.get('MONGO_URI', '')

# Additional Configuration
OWNER_ID = int(os.environ.get('OWNER_ID', '504848353'))
LOG_CHANNEL_ID = int(os.environ.get('LOG_CHANNEL_ID', '-1002971022913'))

