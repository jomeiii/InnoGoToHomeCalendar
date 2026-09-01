from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Сколько осталось?")
        ],
        [
            KeyboardButton(text="🔔 Подписка"),
            KeyboardButton(text="⚙️ Настройки")
        ]
    ],
    resize_keyboard=True
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Изменить дату каникул")
        ],
        [
            KeyboardButton(text="◀️ Назад")
        ]
    ],
    resize_keyboard=True
)