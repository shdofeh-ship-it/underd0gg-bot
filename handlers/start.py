import random
import datetime

import aiosqlite

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import DB_NAME
from keyboards import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT shadow_id FROM users WHERE user_id=?",
            (message.from_user.id,)
        )

        user = await cursor.fetchone()

        if not user:

            shadow_id = f"SHD-{random.randint(1000,9999)}"

            await db.execute(
                """
                INSERT INTO users
                (
                    user_id,
                    username,
                    shadow_id,
                    joined_at
                )
                VALUES(?,?,?,?)
                """,
                (
                    message.from_user.id,
                    message.from_user.username,
                    shadow_id,
                    datetime.datetime.now().strftime("%d.%m.%Y")
                )
            )

            await db.commit()

        else:
            shadow_id = user[0]

    text = f"""
<pre>
██████████████████████

      UNDERD0GG

No Face.
No Limits.

██████████████████████

Shadow ID:
{shadow_id}

SYSTEM STATUS:
ONLINE

Nobody Knows.
Everybody Watches.
</pre>
"""

    await message.answer(
        text,
        reply_markup=main_menu()
    )
