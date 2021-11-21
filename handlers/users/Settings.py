import time

from keyboards.inline.settings import settings
from loader import dp,bot
from aiogram.types import Message
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
