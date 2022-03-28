import motor.motor_asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

Token = "2116108866:AAEkAyI1ufoJrEmfOpO227EBBjMIbT7iPgo"
bot = Bot(token=Token)
dp = Dispatcher(bot)

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://Khamidullo:khamid007@carservice.7ajy9.mongodb.net"
                                                 "/myFirstDatabase?retryWrites=true&w=majority")
collection = cluster.CarService.Customers


@dp.message_handler(commands='start')
async def say_hello(msg: types.Message):
    await msg.answer("You have been added to database")
    user_id = msg.from_user.id
    name = msg.from_user.full_name
    await add_user(user_id, name)


async def add_user(user_id, name):
    date = datetime.now().date()
    collection.insert_one(
        {"_id": user_id,
         "name": name,
         "date": str(date)}
    )


print("Bot is running")
executor.start_polling(dp)
