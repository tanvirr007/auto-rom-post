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

def validate_bot_token(bot_token):
    """Validate the bot token by making a test API call."""
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Seems like your Telegram bot token is wrong.")
    return response.json()
