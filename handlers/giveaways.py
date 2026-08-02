from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import back_keyboard

router = Router()


@router.callback_query(F.data == "giveaways")
async def giveaways(callback: CallbackQuery):

    text = """
<pre>
██████████████████████

      GIVEAWAYS

██████████████████████

🎁 Активных розыгрышей:
0

🏆 Завершенных:
0

⚡ Скоро здесь появятся
реальные розыгрыши.

UNDERD0GG
</pre>
"""

    await callback.message.edit_text(
        text,
        reply_markup=back_keyboard()
    )
