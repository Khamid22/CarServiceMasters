from aiogram.dispatcher.filters.state import StatesGroup, State


class Settings(StatesGroup):
    setting_panel = State()
    car_panel = State()
    date = State()
    service_panel = State()