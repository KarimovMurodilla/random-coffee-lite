from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db


# ---Activity---
# @dp.message_handler(chat_id=ADMINS, commands='activity', state='*')
# async def bot_activity(message: types.Message, state: FSMContext):
#     url = gs.get_url()
#     await message.answer(url)