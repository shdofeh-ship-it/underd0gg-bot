from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import aiosqlite

router = Router()

DB_NAME = "underd0gg.db"


@router.callback_query(F.data == "giveaways")
async def giveaways(callback: CallbackQuery):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, title, prize FROM giveaways WHERE active=1"
        )
        rows = await cursor.fetchall()

    if not rows:
        await callback.message.edit_text("🎁 Активных розыгрышей нет.")
        await callback.answer()
        return

    text = "🎁 <b>Активные розыгрыши</b>\n\n"

    kb = InlineKeyboardBuilder()

    for giveaway in rows:
        gid, title, prize = giveaway

        text += f"🏆 <b>{title}</b>\n"
        text += f"🎁 {prize}\n\n"

        kb.button(
            text=f"Участвовать #{gid}",
            callback_data=f"join_{gid}"
        )

    kb.adjust(1)

    await callback.message.edit_text(
        text,
        reply_markup=kb.as_markup()
    )

    await callback.answer()


@router.callback_query(F.data.startswith("join_"))
async def join(callback: CallbackQuery):
    giveaway_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id

    async with aiosqlite.connect(DB_NAME) as db:
        try:
            await db.execute(
                "INSERT INTO participants(giveaway_id, user_id) VALUES(?, ?)",
                (giveaway_id, user_id)
            )

            await db.execute(
                "UPDATE users SET participations = participations + 1 WHERE user_id=?",
                (user_id,)
            )

            await db.commit()

            await callback.answer("✅ Вы участвуете!", show_alert=True)

        except:
            await callback.answer("Вы уже участвуете.", show_alert=True)
