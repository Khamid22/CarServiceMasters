from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.master_panel import returns_back
from keyboards.inline.master_panel import admin_menu, reject
from states.Master import admin_panel
from aiogram.types import CallbackQuery
from loader import dp, Database as db


@dp.callback_query_handler(text="register", state=admin_panel.register)
async def registration(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Enter the password below: </b>")
    await admin_panel.secret_key.set()

# Master's profile settings

