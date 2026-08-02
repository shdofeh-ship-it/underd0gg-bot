import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Теперь токен берется из переменных окружения, а не из кода!
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID администраторов
ADMIN_IDS = [
    1053853724    
]

# Ссылки
KICK_URL = "https://kick.com/underd0gg"

YOUTUBE_SHORTS = [
    "https://youtube.com/shorts/VIDEO1",
    "https://youtube.com/shorts/VIDEO2",
]

TIKTOK = [
    "https://tiktok.com/@underd0gg/video1",
    "https://tiktok.com/@underd0gg/video2",
]
