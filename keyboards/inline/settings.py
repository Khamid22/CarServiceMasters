from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import Database as db
settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Car Categories", callback_data="category"),
            InlineKeyboardButton(text="Services", callback_data="Services")
        ],
        [
            InlineKeyboardButton(text="Date/Time", callback_data="date_time")
        ],
        [
            InlineKeyboardButton(text="Masters", callback_data="masters"),
            InlineKeyboardButton(text="Black list", callback_data="black")
        ]
    ]
)


def delete(master_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Warning ⚠️", callback_data=f"warning#{master_id}"),
                InlineKeyboardButton(text="Ban ⛔️", callback_data=f"ban#{master_id}"),
            ],
            [
                InlineKeyboardButton(text="🔙Back", callback_data="🔙Back")
            ]
        ]
    )
    return keyboard


# List of available services
async def services_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    list_services = await db.list_of_services()
    for service in list_services:
        keyboard.insert(InlineKeyboardButton(service.get("name"), callback_data=f"settings_service{service.get('id')}"))
    keyboard.insert(InlineKeyboardButton(text="🔙Back", callback_data="🔙Back"))
    return keyboard


# List of available car categories
async def cars():
    keyboard = InlineKeyboardMarkup(row_width=3)
    car_categories = await db.list_of_cars()
    for car in car_categories:
        keyboard.insert(InlineKeyboardButton(car.get("car_category"), callback_data=f"settings_car{car.get('id')}"))
    keyboard.insert(InlineKeyboardButton(text="🔙Back", callback_data="🔙Back"))
    return keyboard

cancel = InlineKeyboardMarkup(row_width=1)
cancel.insert(InlineKeyboardButton(text="cancel", callback_data="cancel1"))


async def dates():
    keyboard = InlineKeyboardMarkup(row_width=3)
    week = await db.list_of_days()
    for day in week:
        keyboard.insert(InlineKeyboardButton(day.get("date/time"), callback_data=f"settings_date{day.get('id')}"))
    keyboard.insert(InlineKeyboardButton(text="🔙Back", callback_data="🔙Back"))
    return keyboard
cancel2 = InlineKeyboardMarkup(row_width=1)
cancel2.insert(InlineKeyboardButton(text="cancel", callback_data="cancel2"))


# back button(from masters to main settings control)
get_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Back", callback_data="🔙Back")
        ]
    ]
)

# back button
back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Back", callback_data="back*")
        ]
    ]
)


# Unblocking the user by id number
def unblock(master_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.insert(InlineKeyboardButton(text="Unblock", callback_data=f"unblock#{master_id}"))
    return keyboard
