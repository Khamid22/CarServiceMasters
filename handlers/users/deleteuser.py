from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline.master_panel import admin_menu
from keyboards.inline.newuser import cancel
from states.Master import admin_panel
from loader import dp, Database as db, bot


@dp.callback_query_handler(text='delete', state=admin_panel.mainmenu)
async def delete_account(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>ð® DO YOU REALLY WANT TO DELETE YOUR ACCOUNT?</b>"
                              "\n    \n"
                              "<i>CHANGES ARE IRREVERSIBLE AND ALL YOUR DATA WILL BE DELETED âï¸</i>",
                              reply_markup=cancel)
    await call.answer(cache_time=60)
    await admin_panel.delete.set()


# Deletes user's account after receiving the confirmation
@dp.callback_query_handler(text='yes', state=admin_panel.delete)
async def confirm(call: CallbackQuery, state: FSMContext):
    master_id = call.from_user.id
    await call.message.delete()
    await db.delete_account(master_id)
    await call.message.answer("Your account has been deleted, thank you for your collaboration.")
    await call.answer(cache_time=60)
    await state.finish()


# User cancel the process and gets back to the main menu
@dp.callback_query_handler(text='cancel', state=admin_panel.delete)
async def cancels(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
    await call.message.answer_photo(photo_url, caption='The master mode has been activated â: \n'
                                                       f'<b>Master ID : {call.from_user.id}</b>'
                                                       '\n     \n'
                                                       '<i>âï¸We highly recommend to set your profile first '
                                                       'if you have not done it yet, because customers can get in '
                                                       'touch with you directly looking at your profile.</i>',
                                    reply_markup=admin_menu)
    await admin_panel.mainmenu.set()
