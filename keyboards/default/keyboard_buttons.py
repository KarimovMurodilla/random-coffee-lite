from aiogram import types


def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Регистрация")
    btn2 = types.KeyboardButton("Посмотреть участников")
    btn3 = types.KeyboardButton("Расписание")
    menu.add(btn1, btn2, btn3)

    return menu


def check_name():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Верно")
    btn2 = types.KeyboardButton("Исправить")
    menu.add(btn1, btn2)

    return menu


def poll():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Постоянно")
    btn3 = types.KeyboardButton("Часто бываю")
    btn4 = types.KeyboardButton("Иногда бываю")
    btn5 = types.KeyboardButton("Нет, но скоро приеду")
    btn6 = types.KeyboardButton("Нет")
    btn7 = types.KeyboardButton("Не живу")
    menu.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    return menu
