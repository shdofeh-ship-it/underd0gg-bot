import aiosqlite

from aiogram import Router, F
from aiogram.types import Message

from database import DB_NAME

router = Router()


@router.message(F.text == "👤 Мой профиль")
async def profile(message: Message):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            """
            SELECT shadow_id, wins, participations
            FROM users
            WHERE user_id=?
            """,
            (message.from_user.id,)
        )

        user = await cursor.fetchone()

    if not user:
        await message.answer("Профиль не найден. Используйте /start")
        return

    shadow_id, wins, participations = user

    await message.answer(
        f"""
<pre>
UNDERD0GG PROFILE

Shadow ID:
{shadow_id}

Участий:
{participations}

Побед:
{wins}

STATUS:
SHADOW MEMBER
</pre>
"""
    )
