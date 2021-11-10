from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

returns_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Back')
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)