from aiogram import Router
from aiogram.types import Message
from aiogram import F

router = Router()


@router.message(F.text == "🔴 Статус стрима")
async def stream_status(message: Message):
    await message.answer(
        "🔴 <b>STREAM STATUS</b>\n\n"
        "SYSTEM: ONLINE\n\n"
        "Kick:\n"
        "https://kick.com/underd0gg"
    )


@router.message(F.text == "⚙️ Настройки")
async def settings(message: Message):
    await message.answer(
        "⚙️ Настройки будут доступны в следующем обновлении."
    )


@router.message(F.text == "🔗 Ресурсы")
async def resources(message: Message):
    await message.answer(
        "🌐 UNDERD0GG NETWORK\n\n"
        "Kick\n"
        "YouTube\n"
        "TikTok\n\n"
        "Ссылки добавим позже."
    )
