import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from database import init_db

from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.profile import router as profile_router
from handlers.giveaways import router as giveaways_router
from handlers.promo import router as promo_router
from handlers.admin import router as admin_router
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    # Инициализация базы данных
    await init_db()

    # Подключение роутеров
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(profile_router)
    dp.include_router(giveaways_router)
    dp.include_router(promo_router)
    dp.include_router(admin_router)
    print("UNDERD0GG BOT ONLINE")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
