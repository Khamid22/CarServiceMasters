from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.master_panel import returns_back
from keyboards.inline.master_panel import admin_menu, reject, get_back
from keyboards.inline.newuser import submit
from states.Master import admin_panel
from states.new_user import new_User
from aiogram.types import CallbackQuery
from loader import dp, Database as db, bot


@dp.callback_query_handler(text="register", state=admin_panel.register)
async def registration(call: CallbackQuery, state: FSMContext):
    await call.message.answer("<b>Enter the password below: </b>")
    await call.message.delete()
    await admin_panel.secret_key.set()


# Master's profile settings
@dp.callback_query_handler(text='profile', state=admin_panel.mainmenu)
async def set_profile(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f'<b>👨🏻‍🔧 Welcome,{call.from_user.full_name}</b>\n  \n'
                              f'<b>🚸 Step 1</b> of 5\n  \n'
                              f'<i>😊 Write your name here: </i>\n  \n'
                              f'<i>✍🏻 Example: Khamidullo</>',reply_markup=get_back)
    await bot.edit_message_text()
    await new_User.full_name.set()


@dp.callback_query_handler(text='name', state=new_User.full_name)
async def full_name(call: CallbackQuery, state: FSMContext):
    name = call.message.text
    await state.update_data(
        {"name": name}
    )
    await call.message.delete()
    await call.message.answer(f'<b>🚸 Step 2</b> of 5\n  \n'
                              f'<i>😊 Write your phone number here: </i>\n  \n'
                              f'<i>✍🏻 Example: +998(xx)-xxx-xx-xx</i>', reply_markup=get_back)
    await new_User.phone_number.set()


@dp.message_handler(state=new_User.phone_number)
async def phone_number(message: Message, state: FSMContext):
    try:
        number = int(message.text)
        await state.update_data(
            {"number": number}
        )
        await message.delete()
        await message.answer(f'<b>🚸 Step 3</b> of 5\n  \n'
                                  f'<i>😊 Write your work experience here: </i>\n  \n'
                                  f'<i>✍🏻 Example: 2 years</i>',reply_markup=get_back)
        await new_User.Work_Experience.set()

    except ValueError:
        await message.answer("Please enter a valid phone number! ")


@dp.message_handler(state=new_User.Work_Experience)
async def full_name(message: Message, state: FSMContext):
    experience = message.text
    await state.update_data(
        {"Work-experience": experience}
    )
    await message.delete()
    await message.answer(f'<b>🚸 Step 4</b> of 5\n  \n'
                              f'<i>😊 Write the name of car service you work?: </i>\n  \n'
                              f'<i>✍🏻 Example: Ferrari-autoservice</i>', reply_markup=get_back)
    await new_User.ServiceName.set()


@dp.message_handler(state=new_User.ServiceName)
async def full_name(message: Message, state: FSMContext):
    car_service = message.text
    await state.update_data(
        {"CarService": car_service}
    )
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("number")
    experience = data.get("Work-experience")
    service = data.get("CarService")

    msg = f"ID: {message.from_user.id}\n"
    msg += f"Name - {name} \n"
    msg += f"Phone - {phone}\n"
    msg += f"Experience - {experience}\n"
    msg += f"Service - {service}\n"

    await message.answer(msg, reply_markup=submit)
    await new_User.Confirm.set()


@dp.callback_query_handler(text='submit', state=new_User.Confirm)
async def submit_the_info(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=admin_menu)
    await call.answer(
        "The profile has been updated<",
        cache_time=60, show_alert=True
    )
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    experience = data.get("Work-experience")
    service = data.get("CarService")
    admin_id = call.from_user.id
    await db.update_profile(name, phone, experience, service, admin_id)
    await state.finish()


@dp.callback_query_handler(text='cancel', state=new_User.Confirm)
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=admin_menu)
    await call.answer("The process has been canceled", cache_time=60, show_alert=True)
    await state.finish()


@dp.callback_query_handler(text='return', state='*')
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo_url = "https://hireology.com/wp-content/uploads/2017/08/38611898_m-1.jpg"
    await call.message.answer_photo(photo_url, caption='The master mode has been activated ✅: \n'
                                                  f'<b>Master ID : {call.from_user.id}</b>'
                                                  '\n     \n'
                                                  '<i>❗️We highly recommend to set your profile first '
                                                  'if you have not done it yet, because customers can get in '
                                                  'touch with you directly looking at your profile.</i>',
                               reply_markup=admin_menu)
    await admin_panel.mainmenu.set()
