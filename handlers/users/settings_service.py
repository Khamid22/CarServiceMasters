from keyboards.inline.settings import settings, services_keyboard, back
from loader import dp, Database as db, bot
from aiogram.types import Message, CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext

photo_url = "https://i.pinimg.com/originals/e9/55/b8/e955b8bf79636c2f6ac0ff2d0bf5fb9b.png"


@dp.callback_query_handler(text="Services", state=Settings.setting_panel)
async def list_of_services(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except:
        pass
    msg = "List of available services:"
    keyboard = await services_keyboard()
    await call.message.answer(msg, reply_markup=keyboard)


@dp.callback_query_handler(text_startswith='setting_service', state='*')
async def setting_service(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except:
        pass
    service_id = call.data.replace('setting_service', '')
    await call.message.answer(f'<i>😊 Enter new service name: </i>',reply_markup=back)
    async with state.proxy() as data:
        data['service_id'] = service_id
    await Settings.service_panel.set()


@dp.message_handler(content_types='text', state=Settings.service_panel)
async def new_settings(message: Message, state: FSMContext):
    try:
        chat_id = message.chat.id
        message_id = message.message_id
        await bot.delete_message(chat_id, message_id)
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
async def get_back(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        await bot.delete_message(chat_id, message_id)
    except:
        pass
    msg = "List of available services:"
    keyboard = await services_keyboard()
    await call.message.answer(msg, reply_markup=keyboard)