import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from database import init_db

# Импорт роутеров (пока подключаем только start)
from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.profile import router as profile_router
async def main():
    # Логирование
    logging.basicConfig(...)

    # Создаем бота
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    # Создаем диспетчер
    dp = Dispatcher()

    # Подключаем базу
    await init_db()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(profile_router)

    print("UNDERD0GG BOT ONLINE")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
