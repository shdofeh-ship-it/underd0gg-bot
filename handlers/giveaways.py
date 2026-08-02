import aiosqlite

from aiogram import Router, F
from aiogram.types import CallbackQuery

from database import DB_NAME
from keyboards import back_keyboard

router = Router()


@router.callback_query(F.data == "giveaways")
async def giveaways(callback: CallbackQuery):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute("""
            SELECT id, title, prize
            FROM giveaways
            WHERE active = 1
        """)

        giveaways = await cursor.fetchall()

    if not giveaways:

        await callback.message.edit_text(
            """
<pre>
████████████████████

🎁 GIVEAWAYS

━━━━━━━━━━━━━━━━━━━━

Сейчас нет
активных розыгрышей.

Следи за обновлениями.

UNDERD0GG
</pre>
""",
            reply_markup=back_keyboard()
        )

        return

    text = "<b>🎁 Активные розыгрыши</b>\n\n"

    for giveaway in giveaways:
        text += (
            f"🎯 <b>{giveaway[1]}</b>\n"
            f"🎁 Приз: {giveaway[2]}\n\n"
        )

    await callback.message.edit_text(
        text,
        reply_markup=back_keyboard()
    )
