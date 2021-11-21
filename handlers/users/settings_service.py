from keyboards.inline.settings import settings, services_keyboard, back
from loader import dp, Database as db, bot
from aiogram.types import Message, CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext

photo_url = "https://i.pinimg.com/originals/e9/55/b8/e955b8bf79636c2f6ac0ff2d0bf5fb9b.png"


@dp.callback_query_handler(text="Services", state=Settings.setting_panel)
async def list_of_services(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    msg = "List of available services:"
    keyboard = await services_keyboard()
    await call.message.answer(msg, reply_markup=keyboard)


@dp.callback_query_handler(text_startswith='settings_service', state='*')
async def setting_service(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    except:
        pass
    service_id = call.data.replace('settings_service', '')
    await call.message.answer(f'<i>😊 Enter new service name: </i>',reply_markup=back)
    async with state.proxy() as data:
        data['service_id'] = service_id
    await Settings.service_panel.set()


@dp.message_handler(content_types='text', state=Settings.service_panel)
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
        service_id = data['service_id']
    await db.apply("update services set name=%s where id=%s", (new_name, service_id))
    msg = "List of available services:"
    keyboard = await services_keyboard()
    await message.answer(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="🔙Back", state="*")
async def return_back(call: CallbackQuery):
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 2, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await call.message.answer_photo(photo_url, caption="Bot settings", reply_markup=settings)
    await Settings.setting_panel.set()


@dp.callback_query_handler(text="back*", state="*")
async def get_back(call: CallbackQuery):
    await call.message.delete()
    msg = "List of available services:"
    keyboard = await services_keyboard()
    await call.message.answer(msg, reply_markup=keyboard)