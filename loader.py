from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db_commands import MySQLStorage
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
Database: MySQLStorage = MySQLStorage("telegrambot", user='customers', password='0TGA0(DAAgG2@M7G')