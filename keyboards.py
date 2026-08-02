from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔴 Статус стрима"),
            KeyboardButton(text="🎁 Розыгрыши")
        ],
        [
            KeyboardButton(text="💰 Промокоды"),
            KeyboardButton(text="🏆 Победители")
        ],
        [
            KeyboardButton(text="👤 Мой профиль"),
            KeyboardButton(text="🔗 Ресурсы")
        ],
        [
            KeyboardButton(text="⚙️ Настройки")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите раздел..."
)
