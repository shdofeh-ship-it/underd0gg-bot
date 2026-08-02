from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import main_menu, back_keyboard
from config import KICK_URL

router = Router()


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    text = """
<pre>
██████████████████████

      UNDERD0GG

No Face.
No Limits.

██████████████████████

SYSTEM STATUS:
ONLINE

Nobody Knows.
Everybody Watches.
</pre>
"""

    await callback.message.edit_text(
        text,
        reply_markup=main_menu()
    )


@router.callback_query(F.data == "status")
async def status(callback: CallbackQuery):
    await callback.message.edit_text(
        f"""
<b>🔴 STREAM STATUS</b>

STATUS:
🟢 ONLINE

🎥 Kick:
{KICK_URL}
""",
        reply_markup=back_keyboard()
    )


@router.callback_query(F.data == "resources")
async def resources(callback: CallbackQuery):
    await callback.message.edit_text(
        """
<b>🌐 UNDERD0GG NETWORK</b>

🎥 Kick
▶ YouTube Shorts
🎵 TikTok

Ссылки будут добавлены позже.
""",
        reply_markup=back_keyboard()
    )


@router.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):
    await callback.message.edit_text(
        """
<b>⚙ SETTINGS</b>

Раздел находится в разработке.
""",
        reply_markup=back_keyboard()
    )
