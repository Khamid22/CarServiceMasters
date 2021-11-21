import time

from keyboards.inline.settings import settings, delete
from loader import dp, Database as db, bot
from aiogram.types import Message, CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext

photo_url = "https://i.pinimg.com/originals/e9/55/b8/e955b8bf79636c2f6ac0ff2d0bf5fb9b.png"


# Secret key to settings panel
@dp.message_handler(commands="settings!", state="*")
async def setting(message: Message, state: FSMContext):
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 2, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await message.answer_photo(photo_url, caption="Bot settings", reply_markup=settings)
    await Settings.setting_panel.set()


@dp.callback_query_handler(text="masters", state=Settings.setting_panel)
async def masters(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        await bot.delete_message(chat_id, message_id)
    except:
        pass
    technicians = await db.all_masters()
    for master in technicians:
        master_id = master.get("admin_id")
        full_name = master.get("full_name")
        phone = master.get("phone_number")
        experience = master.get("Work_Experience")
        workshop = master.get("ServiceName")
        location = master.get("Locaiton")

        msg = f"<b>Master ID: {master_id} </b>\n" \
              "  ➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
        msg += f"Name: {full_name}\n"
        msg += f"Mobile: {phone}\n"
        msg += f"Experience: {experience}\n"
        msg += f"Workshop: {workshop}\n"
        msg += f"Location:{location}"
        time.sleep(0.8)
        await call.message.answer(msg, reply_markup=delete(master_id))
        await Settings.setting_panel.set()
