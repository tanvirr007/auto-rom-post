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

def format_caption():
    """Generate the formatted text template."""
    today = datetime.now().strftime("%d/%m/%y")
    caption = f"""

#crDroid #spes #spesn #A15 #VIC #UNOFFICIAL #OSS
*crDroid 11.x | UNOFFICIAL | Android 15*
*Released:* _{today}_'

▪️Download
▪️Screenshots
▪️[Support Group](https://t.me/TanvirBuildsSupport)
▪️[Update Channel](https://t.me/Tanvir_CI)

*Changelog:*
• Type Here
• Type Here

*Notes:*
• Don't forget to backup your important data
• Use [PIF](https://t.me/TanvirBuilds/435) if needed
• Use official [OrangeFox](https://orangefox.download/device/spes) recovery
• Report bugs with proper logs
• If you like our work, consider [donating](https://github.com/Team-Remix/.github/blob/main/donation%2FDONATION.md) to support server costs
• This is an automatically generated post

*Credits:*
• All spes devs for resources
• All of my testers for testing
• Special thanks to God, Sun, Time, Love and Spes

*By* [@tanvirr007](https://t.me/tanvirr007)
*Follow* [@TanvirBuilds](https://t.me/TanvirBuilds)
*Join* [@TanvirBuildsSupport](https://t.me/TanvirBuildsSupport)
"""
    return caption

def send_photo_with_caption(bot_token, chat_id, photo_path, caption):
    """Send a photo with a caption to a Telegram chat."""
    if not os.path.exists(photo_path):
        raise FileNotFoundError(f"File '{photo_path}' not found.")

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    with open(photo_path, "rb") as photo:
        response = requests.post(
            url,
            data={"chat_id": chat_id, "caption": caption, "parse_mode": "Markdown"},
            files={"photo": photo}
        )

    if response.status_code != 200:
        raise Exception(
            f"Failed to send photo. HTTP Status: {response.status_code}, Response: {response.text}"
        )
    return response.json()

if __name__ == "__main__":
    try:

        BOT_TOKEN = get_bot_token()

        validate_bot_token(BOT_TOKEN)

        caption = format_caption()

        response = send_photo_with_caption(BOT_TOKEN, CHAT_ID, BANNER_PATH, caption)
        print("Photo sent successfully. Response:", response)

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")
        print("Please check your Telegram bot token and try again.")

        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
        print(f"The token file '{TOKEN_FILE}' has been removed. Please enter the correct token next time.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
