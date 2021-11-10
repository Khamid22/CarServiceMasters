from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
import time

from keyboards.default.master_panel import returns_back
from keyboards.inline.master_panel import admin_menu, reject
from states.Master import admin_panel
from aiogram.types import CallbackQuery
from loader import dp, Database as db


# Registers new users
@dp.message_handler(text_contains="Password 🔐", state=admin_panel.register)
async def registration(message: Message, state: FSMContext):
    await message.delete()
    await message.answer("<b>Enter the password below: </b>", reply_markup=ReplyKeyboardRemove(True))
    await admin_panel.secret_key.set()


# Checks the incoming messages and compares
@dp.message_handler(state=admin_panel.secret_key)
async def password(message: Message, state: FSMContext):
    secret_key = message.text
    pass_key = "master007"
    await message.delete()
    if secret_key == pass_key:
        photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
        await message.answer_photo(photo_url, caption='The master mode has been activated ✅: '
                                                      '\n     \n'
                                                      '<i>❗️We highly recommend to set your profile first '
                                                      'if you have not done it yet, because customers can get in '
                                                      'touch with you directly looking at your profile.</i>',
                                   reply_markup=admin_menu)
        await db.apply(
            "insert into masters(admin_id) values(%s)",
            message.from_user.id
                )
        await admin_panel.reservations.set()
    else:
        await message.answer('<i>❌ Invalid password,try again</i>')


# Shows list of reservations
@dp.callback_query_handler(text="clients", state=admin_panel.reservations)
async def show_customer(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("List of recent customers: ", reply_markup=returns_back)
    customers = await db.all_customers()
    for customer in customers:
        customer_id = customer.get("user_id")
        name = customer.get("name")
        car = customer.get("car")
        phone_number = customer.get("phone_number")
        service2 = customer.get("service")
        date2 = customer.get("date")

        msg = "Customer's info📝: \n"
        msg += f"Client👤- {name}\n"
        msg += f"Car🚗 - {car}\n"
        msg += f"Phone-number📞 - {phone_number}\n"
        msg += f"Service🛠 - {service2}\n"
        msg += f"Date/time⏱ - {date2}"
        time.sleep(1)
        await call.message.answer(msg, reply_markup=reject(customer_id))


# Rejects the reservation of a customer and notifies the rejection back
@dp.callback_query_handler(text_contains='reject', state=admin_panel.reservations)
async def reject_customer(call: CallbackQuery, state: FSMContext):
    customer_id = call.data.split('#')[1]

    await call.message.delete()
    await db.delete_customer(customer_id)
    await call.answer("Customer rejected successfully", cache_time=60, show_alert=True)
    try:
        await dp.bot.send_message(chat_id=customer_id, text="Apparently, your reservation has been rejected due to "
                                                            "some mistakes, please provide more accurate data ‼️")

    except:

        await call.message.answer(f"Can't notify the {customer_id} id user")


@dp.message_handler(text='🔙 Back', state=admin_panel.reservations)
async def returns(message: Message, state: FSMContext):
    await message.delete()
    photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
    await message.answer_photo(photo_url, caption='The master mode has been activated ✅: ', reply_markup=admin_menu)