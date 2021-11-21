from keyboards.inline.settings import dates, cars, cancel2
from loader import dp, Database as db, bot
from aiogram.types import Message, CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="date_time", state=Settings.setting_panel)
async def date(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    keyboard = await dates()
    await call.message.answer("<b>Set appropriate date/time for your customers</b>", reply_markup=keyboard)


@dp.callback_query_handler(text_startswith='settings_date', state='*')
async def setting_service(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    date_id = call.data.replace('settings_date', '')
    await call.message.answer(f'<i>😊 Enter new date and time: </i>', reply_markup=cancel2)
    async with state.proxy() as data:
        data['date_id'] = date_id
    await Settings.date.set()


@dp.message_handler(content_types='text', state=Settings.date)
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
        date_id = data['date_id']
    await db.apply("update cars set car_category=%s where id=%s", (new_name, date_id))
    msg = "List of available car categories:"
    keyboard = await dates()
    await message.answer(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="cancel2", state="*")
async def cancels(call: CallbackQuery):
    await call.message.delete()
    keyboard = await dates()
    await call.message.answer("<b>Set appropriate date/time for your customers</b>", reply_markup=keyboard)