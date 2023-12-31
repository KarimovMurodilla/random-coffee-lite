from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(
        "Commands:\n"
        "/start - Start bot\n"
        "/help - Help"
    )