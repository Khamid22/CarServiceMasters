import time
from keyboards.inline.settings import delete, settings, get_back, unblock
from loader import dp, Database as db
from aiogram.types import CallbackQuery
from states.settings import Settings
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="black", state=Settings.setting_panel)
async def black_list(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    banned_masters = await db.black_list()
    if not banned_masters:
        await call.message.answer("No banned masters here", reply_markup=get_back)
    else:
        for user in banned_masters:
            master_id = user.get("master_id")
            full_name = user.get("full_name")

            await call.message.answer(f"User was banned for breaking the rules of administration:\n \n"
                                      f"Master ID: {master_id}\n \n"
                                      f"Full name: {full_name}\n", reply_markup=unblock(master_id))
            await Settings.setting_panel.set()


@dp.callback_query_handler(text_contains="unblock", state="*")
async def unblocking(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    master_id = call.data.split("#")[1]
    await db.user_unblock(master_id)
    await call.answer(f"The technician with the id: {master_id} has been unlocked", cache_time=60, show_alert=True)
    await dp.bot.send_message(master_id, "Your account has been unlocked")
    await state.finish()