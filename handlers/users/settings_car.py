from keyboards.inline.settings import cars, cancel
from loader import dp, Database as db, bot
from aiogram.types import Message, CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="category", state=Settings.setting_panel)
async def car_category(call: CallbackQuery):
    await call.message.delete()
    keyboard = await cars()
    await call.message.answer("List of available car categories: ", reply_markup=keyboard)


@dp.callback_query_handler(text_startswith='settings_car', state='*')
async def setting_service(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    car_id = call.data.replace('settings_car', '')
    await call.message.answer(f'<i>😊 Enter new car category: </i>', reply_markup=cancel)
    async with state.proxy() as data:
        data['car_id'] = car_id
    await Settings.car_panel.set()


@dp.message_handler(content_types='text', state=Settings.car_panel)
async def new_settings(message: Message, state: FSMContext):
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 2, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    new_name = message.text
    async with state.proxy() as data:
        car_id = data['car_id']
    await db.apply("update cars set car_category=%s where id=%s", (new_name, car_id))
    msg = "List of available car categories:"
    keyboard = await cars()
    await message.answer(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="cancel1", state="*")
async def cancels(call: CallbackQuery):
    await call.message.delete()
    keyboard = await cars()
    await call.message.answer("List of available car categories: ", reply_markup=keyboard)