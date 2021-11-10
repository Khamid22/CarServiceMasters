from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

password = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Password 🔐"),
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)

returns_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Back')
        ],
    ]
)