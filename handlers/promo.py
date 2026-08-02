from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import back_keyboard

router = Router()


@router.callback_query(F.data == "promo")
async def promo(callback: CallbackQuery):

    text = """
<pre>
████████████████████

🎟 PROMO CODES

━━━━━━━━━━━━━━━━━━━━

Здесь можно будет
активировать
промокод.

Функция скоро
станет доступна.

UNDERD0GG
</pre>
"""

    await callback.message.edit_text(
        text,
        reply_markup=back_keyboard()
    )
