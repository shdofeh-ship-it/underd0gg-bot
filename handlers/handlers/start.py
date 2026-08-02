import random
from datetime import datetime

import aiosqlite

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import DB_NAME

router = Router()


def generate_shadow_id():
    chars = string.hexdigits.upper().replace("X", "")[:16]
    return "SHD-" + "".join(random.choice(chars) for _ in range(4))


@router.message(CommandStart())
async def start(message: Message):

    user = message.from_user

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT shadow_id FROM users WHERE user_id=?",
            (user.id,)
        )

        row = await cursor.fetchone()

        if row is None:

            shadow_id = generate_shadow_id()

            await db.execute(
                """
                INSERT INTO users(
                    user_id,
                    username,
                    shadow_id,
                    joined_at
                )
                VALUES(?,?,?,?)
                """,
                (
                    user.id,
                    user.username,
                    shadow_id,
                    datetime.utcnow().isoformat()
                )
            )

            await db.commit()

        else:
            shadow_id = row[0]

    text = f"""
<pre>
██████████████████

UNDERD0GG

SYSTEM ONLINE

Identity:
UNKNOWN

Shadow ID:
{shadow_id}

STATUS:
ACCESS GRANTED

No Face.
No Limits.

██████████████████
</pre>
"""

    await message.answer(text)
