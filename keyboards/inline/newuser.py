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

    ]
)


def update(admin_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            InlineKeyboardButton(text='Update', callback_data=f'update#{admin_id}')
        ]
    )
