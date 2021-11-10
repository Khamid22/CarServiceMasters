from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

new_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Full_name', callback_data='name'),
            InlineKeyboardButton(text='Phone Number', callback_data='number'),
        ],
        [
            InlineKeyboardButton(text='CarService', callback_data='service'),
            InlineKeyboardButton(text='WorkExperience', callback_data='experience')
        ],
        [
            InlineKeyboardButton(text='Update', callback_data='Update')
        ]
    ]
)

register = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Password 🔐', callback_data='register')
        ]
    ]
)

cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Yes, I do ✅', callback_data='yes'),
            InlineKeyboardButton(text='Cancel ❌', callback_data='cancel'),
        ]
    ]
)
