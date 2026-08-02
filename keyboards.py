from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👤 Профиль",
                    callback_data="profile"
                ),
                InlineKeyboardButton(
                    text="🎁 Розыгрыши",
                    callback_data="giveaways"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💰 Промокоды",
                    callback_data="promo"
                ),
                InlineKeyboardButton(
                    text="🏆 Победители",
                    callback_data="winners"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔴 Статус",
                    callback_data="status"
                ),
                InlineKeyboardButton(
                    text="🔗 Ресурсы",
                    callback_data="resources"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Настройки",
                    callback_data="settings"
                )
            ]
        ]
    )


def back_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅ Назад",
                    callback_data="back"
                )
            ]
        ]
    )
