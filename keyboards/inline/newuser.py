from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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


submit = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Submit ✅", callback_data="submit"),
            InlineKeyboardButton(text="Cancel ❌", callback_data="cancel"),
        ]
    ]
)

update = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Update 🔄", callback_data='update'),
        ],
        [
            InlineKeyboardButton(text="Back 🔙", callback_data='return'),
        ]

    ]
)