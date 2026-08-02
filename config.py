import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID администраторов (через запятую)
ADMIN_IDS = [
    1053853724    
]

# Ссылки (пока заглушки)
KICK_URL = "https://kick.com/underd0gg"

YOUTUBE_SHORTS = [
    "https://youtube.com/shorts/VIDEO1",
    "https://youtube.com/shorts/VIDEO2",
]

TIKTOK = [
    "https://tiktok.com/@underd0gg/video1",
    "https://tiktok.com/@underd0gg/video2",
]
