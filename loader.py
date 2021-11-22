from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db_commands import MySQLStorage
from data import config
bot2 = Bot(token=config.BOT2_TOKEN, parse_mode=types.ParseMode.HTML)
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp2 = Dispatcher(bot2, storage=storage)

Database: MySQLStorage = MySQLStorage("car_service", user='turin', password='qwerty12')
