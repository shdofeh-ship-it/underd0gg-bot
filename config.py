import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = [
    int(x) for x in os.getenv("ADMIN_IDS", "").split(",")
    if x.strip()
]

KICK_URL = os.getenv("KICK_URL")

YOUTUBE_SHORT_1 = os.getenv("YOUTUBE_SHORT_1")
YOUTUBE_SHORT_2 = os.getenv("YOUTUBE_SHORT_2")

TIKTOK_1 = os.getenv("TIKTOK_1")
TIKTOK_2 = os.getenv("TIKTOK_2")
