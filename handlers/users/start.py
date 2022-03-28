from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from data.config import ADMINS
from keyboards.inline.newuser import register
from keyboards.inline.master_panel import admin_menu
from states.Master import admin_panel
from loader import dp, Database as db, bot


# Asks the password for master's panel
@dp.message_handler(CommandStart(), state='*')
async def master(message: Message, state: FSMContext):
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 3, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass

    admin = await dp.bot.get_chat(ADMINS[0])
    is_master = await db.check_user(message.from_user.id)
    is_banned = await db.check_account(message.from_user.id)
    if is_banned:
        await message.answer(f"Sorry your account has been banned")
    elif not is_master:
        await message.answer(f"<b> 🚫 You are not fully registered yet!</b>\n"
                             f"    \n"
                             f"<i>❗️Please for registration, send me your password "
                             f"clarifying you as a car technician given by the admin!</i>"
                             f"\n     \n"
                             f"⁉️If you have not taken your password identification yet, please contact at @{admin.username}",
                             reply_markup=register)
        await admin_panel.register.set()
    else:
        photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
        await message.answer_photo(photo_url, caption='The master mode has been activated ✅: \n'
                                                      f'<b>Master ID : {message.from_user.id}</b>'
                                                      '\n     \n'
                                                      '<i>❗️We highly recommend to set your profile first '
                                                      'if you have not done it yet, because customers can get in '
                                                      'touch with you directly looking at your profile.</i>',
                                   reply_markup=admin_menu)
        await admin_panel.mainmenu.set()
