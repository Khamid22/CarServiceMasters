from aiogram.dispatcher.filters.state import StatesGroup, State


class admin_panel(StatesGroup):
    mainmenu = State()
    secret_key = State()
    register = State()
    delete = State()
