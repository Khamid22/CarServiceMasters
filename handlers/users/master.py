import time

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message

from keyboards.inline.master_panel import admin_menu, reject
from loader import dp, Database as db, bot, dp2
from states.Master import admin_panel


# Checks the incoming messages and compares
from car_service_master.keyboards.inline.master_panel import get_back


@dp.message_handler(state=admin_panel.secret_key)
async def password(message: Message, state: FSMContext):
    secret_key = message.text
    pass_key = "master007"
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 2, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    if secret_key == pass_key:
        photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
        await message.answer_photo(photo_url, caption='The master mode has been activated ✅: \n'
                                                      f'<b>Master ID : {message.from_user.id}</b>'
                                                      '\n     \n'
                                                      '<i>❗️We highly recommend to set your profile first '
                                                      'if you have not done it yet, because customers can get in '
                                                      'touch with you directly looking at your profile.</i>',
                                   reply_markup=admin_menu)
        await db.apply(
            "insert into masters(admin_id) values(%s)",
            message.from_user.id
        )
        await admin_panel.mainmenu.set()
    else:
        await message.answer('<i>❌ Invalid password,try again</i>')


# Shows list of reservations
@dp.callback_query_handler(text="clients", state=admin_panel.mainmenu)
async def show_customer(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    customers = await db.all_customers()
    if not customers:
        await call.message.answer("<b> Nothing to show 🗑</b>", reply_markup=get_back)
    else:
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
@dp.callback_query_handler(text_contains='reject', state=admin_panel.mainmenu)
async def reject_customer(call: CallbackQuery, state: FSMContext):
    customer_id = call.data.split('#')[1]
    row = await db.get("select * from masters where admin_id=%s", customer_id)
    admin_name = row.get("full_name")
    await dp2.bot.send_message(customer_id, f"You have been rejected by one of the masters, maybe something went "
                                            f"wrong....")
    await call.answer(f"[{customer_id}] Customer has been rejected successfully",cache_time=60, show_alert=True)
    await db.delete_customer(customer_id)


@dp.callback_query_handler(text_contains='accept', state=admin_panel.mainmenu)
async def reject_customer(call: CallbackQuery, state: FSMContext):
    customer_id = call.data.split('#')[1]
    row = await db.get("select * from masters where admin_id=%s", customer_id)
    admin_id = row.get("admin_id")
    admin_name = row.get("full_name")
    admin_location = row.get("Location")
    await dp2.bot.send_message(customer_id, f"<i>You have been successful accepted by {admin_name} with the id: {admin_id}\n \n"
                                            f"Location: {admin_location}")
    await call.answer(f"[{customer_id}] Customer has been accepted successfully", cache_time=60, show_alert=True)
    await db.delete_customer(customer_id)
    await db.apply("insert into ")


@dp.callback_query_handler(text='🔙 Back.', state=admin_panel.mainmenu)
async def returns(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
    await call.message.answer_photo(photo_url, caption='The master mode has been activated ✅: \n'
                                                       f'<b>Master ID : {call.message.from_user.id}</b>'
                                                       '\n     \n'
                                                       '<i>❗️We highly recommend to set your profile first '
                                                       'if you have not done it yet, because customers can get in '
                                                       'touch with you directly looking at your profile.</i>',
                                    reply_markup=admin_menu)
