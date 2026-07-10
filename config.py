import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_FILE = os.getenv("DB_FILE", "gatherly.db")
DEFAULT_UI_MODE = os.getenv("DEFAULT_UI_MODE", "full")
