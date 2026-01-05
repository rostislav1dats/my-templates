import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
EXTERNAL_API_URL = ''
WHITELIST = [12345678, 87654321]