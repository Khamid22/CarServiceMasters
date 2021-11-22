from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)
# Main pane commands appear after master successfully logged into server
admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Clients 👨🏼", callback_data='clients'),
            InlineKeyboardButton(text="My Profile 👤", callback_data='profile')
        ],
        [
            InlineKeyboardButton(text='Feedbacks 💬', url="https://t.me/CarServiceFeedbacks"),
        ],
        [
            InlineKeyboardButton(text='Delete Account 🗑', callback_data='delete')
        ]
    ]
)

get_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Back", callback_data='return'),
        ],
    ],
)


# Rejects the customer
def reject(customer_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Accept ✅', callback_data=f"accept#{customer_id}"),
                InlineKeyboardButton(text='Reject ❌', callback_data=f'reject#{customer_id}'),
            ],
            [
                InlineKeyboardButton(text="🔙 Back", callback_data="🔙 Back.")
            ]
        ]
    )
    return keyboard

