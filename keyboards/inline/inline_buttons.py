from aiogram import types


def pagination():
    menu = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    btn2 = types.InlineKeyboardButton(text="Вперёд ▶️", callback_data="next")
    menu.add(btn1, btn2)

    return menu