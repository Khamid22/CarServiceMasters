import time
from keyboards.inline.settings import delete, get_back
from loader import dp, Database as db
from aiogram.types import CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext


photo_url = "https://i.pinimg.com/originals/e9/55/b8/e955b8bf79636c2f6ac0ff2d0bf5fb9b.png"


@dp.callback_query_handler(text="masters", state=Settings.setting_panel)
async def technicians(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    masters = await db.all_masters()
    if not masters:
        await call.message.answer("Nothing to show", reply_markup=get_back)
    else:
        for master in masters:
            master_id = master.get("admin_id")
            full_name = master.get("full_name")
            phone = master.get("phone_number")
            experience = master.get("Work_Experience")
            workshop = master.get("ServiceName")
            location = master.get("Location")

            msg = f"<b>Master ID: {master_id} </b>\n" \
                  "  ➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            msg += f"Name: {full_name}\n"
            msg += f"Mobile: {phone}\n"
            msg += f"Experience: {experience}\n"
            msg += f"Workshop: {workshop}\n"
            msg += f"Location: {location}"
            time.sleep(0.8)
            await call.message.answer(msg, reply_markup=delete(master_id))
            await Settings.setting_panel.set()


@dp.callback_query_handler(text_contains="ban", state="*")
async def user_ban(call: CallbackQuery):
    master_id = call.data.split("#")[1]
    name = call.message.from_user.full_name
    await db.apply("insert into black_list(master_id, full_name) values(%s, %s)", (master_id, name))
    await call.answer(f"The technician with the id: {master_id} has been banned", cache_time=60, show_alert=True)
    await dp.bot.send_message(master_id, f"You have been banned by the administration")
    await db.delete_account(master_id)


@dp.callback_query_handler(text_contains="warning", state="*")
async def send_warning(call: CallbackQuery):
    master_id = call.data.split('#')[1]
    await dp.bot.send_message(master_id, f"⚠️You have been warned!, for further details please contact with the "
                                         f"administration")
    await call.answer(f"The technician with the id: {master_id} has been warned", cache_time=60, show_alert=True)
    await Settings.setting_panel.set()