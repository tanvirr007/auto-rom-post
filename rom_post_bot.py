import os
import requests
from datetime import datetime

CHAT_ID = "-100xxxxxx"
BANNER_PATH = "banner.png"
TOKEN_FILE = os.path.expanduser("~/.telegram.bot.token")

def get_bot_token():
    """Retrieve the bot token from a file or prompt the user to enter it."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as file:
            return file.read().strip()
    else:
        token = input("Enter your Telegram Bot Token: ").strip()
        with open(TOKEN_FILE, "w") as file:
            file.write(token)
        print(f"Token saved to {TOKEN_FILE}.")
        return token
