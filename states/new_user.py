from aiogram.dispatcher.filters.state import StatesGroup, State


class new_User(StatesGroup):
    update = State()
    full_name = State()
    phone_number = State()
    Work_Experience = State()
    ServiceName = State()
    Confirm = State()