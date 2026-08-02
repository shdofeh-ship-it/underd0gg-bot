from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):
    await message.answer(
        """
👤 <b>ВАШ ПРОФИЛЬ</b>

🆔 ID: <code>{}</code>

🎫 Билетов: <b>0</b>

👥 Приглашено: <b>0</b>

🏆 Уровень: <b>SHADOW MEMBER</b>
""".format(message.from_user.id)
    )
