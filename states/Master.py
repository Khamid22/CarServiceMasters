from aiogram.dispatcher.filters.state import StatesGroup, State


class admin_panel(StatesGroup):
    register = State()
    secret_key = State()
    reservations = State()
