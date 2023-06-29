from aiogram import types


def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Регистрация")
    btn2 = types.KeyboardButton("Посмотреть участников")
    btn3 = types.KeyboardButton("Расписание")
    menu.add(btn1, btn2, btn3)

    return menu


def yes_no():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Верно")
    btn2 = types.KeyboardButton("Исправить")
    menu.add(btn1, btn2)

    return menu


def poll():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    # btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Постоянно")
    btn3 = types.KeyboardButton("Часто бываю")
    btn4 = types.KeyboardButton("Иногда бываю")
    btn5 = types.KeyboardButton("Нет, но скоро приеду")
    btn6 = types.KeyboardButton("Нет")
    # btn7 = types.KeyboardButton("Не живу")
    menu.add(btn2, btn3, btn4, btn5, btn6)

    return menu


def request_contact():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Поделиться контактом", request_contact=True)
    menu.add(btn1)

    return menu


def skip():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Пропустить")
    menu.add(btn1)

    return menu