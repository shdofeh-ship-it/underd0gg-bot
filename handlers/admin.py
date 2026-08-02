from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import aiosqlite
import random

from config import ADMIN_IDS

router = Router()

DB_NAME = "underd0gg.db"


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


@router.message(Command("create_giveaway"))
async def create_giveaway(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Доступ запрещён.")
        return

    args = message.text.replace("/create_giveaway", "").strip()

    if "|" not in args:
        await message.answer(
            "Использование:\n"
            "/create_giveaway Название|Приз"
        )
        return

    title, prize = args.split("|", 1)

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT INTO giveaways(title, prize, active)
            VALUES (?, ?, 1)
            """,
            (title.strip(), prize.strip())
        )
        await db.commit()

    await message.answer("✅ Розыгрыш создан!")


@router.message(Command("list_giveaways"))
async def list_giveaways(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Доступ запрещён.")
        return

    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            """
            SELECT id, title, prize, active
            FROM giveaways
            """
        )
        giveaways = await cursor.fetchall()

    if not giveaways:
        await message.answer("Розыгрышей нет.")
        return

    text = "🎁 Список розыгрышей:\n\n"

    for g in giveaways:
        status = "🟢" if g[3] else "🔴"
        text += f"{status} #{g[0]} {g[1]}\n🎁 {g[2]}\n\n"

    await message.answer(text)


@router.message(Command("finish_giveaway"))
async def finish_giveaway(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Доступ запрещён.")
        return

    args = message.text.replace("/finish_giveaway", "").strip()

    if not args.isdigit():
        await message.answer(
            "Использование:\n"
            "/finish_giveaway ID"
        )
        return

    giveaway_id = int(args)

    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            """
            SELECT user_id
            FROM participants
            WHERE giveaway_id = ?
            """,
            (giveaway_id,)
        )
        users = await cursor.fetchall()

        if not users:
            await message.answer("Участников нет.")
            return

        winner = random.choice(users)[0]

        await db.execute(
            """
            INSERT INTO winners(giveaway_id, user_id)
            VALUES (?, ?)
            """,
            (giveaway_id, winner)
        )

        await db.execute(
            """
            UPDATE giveaways
            SET active = 0
            WHERE id = ?
            """,
            (giveaway_id,)
        )

        await db.commit()

    await message.answer(
        f"🏆 Победитель:\n<code>{winner}</code>"
    )
