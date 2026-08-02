import aiosqlite

from aiogram import Router, F
from aiogram.types import CallbackQuery

from database import DB_NAME
from keyboards import back_keyboard

router = Router()


@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            """
            SELECT shadow_id, wins, participations
            FROM users
            WHERE user_id=?
            """,
            (callback.from_user.id,)
        )

        user = await cursor.fetchone()

    if not user:
        await callback.answer("Профиль не найден.", show_alert=True)
        return

    shadow_id, wins, participations = user

    await callback.message.edit_text(
        f"""
<pre>
██████████████████████

UNDERD0GG PROFILE

██████████████████████

Shadow ID:
{shadow_id}

🎟 Участий:
{participations}

🏆 Побед:
{wins}

STATUS:
SHADOW MEMBER

No Face.
No Limits.
</pre>
""",
        reply_markup=back_keyboard()
    )
