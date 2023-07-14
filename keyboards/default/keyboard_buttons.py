from aiogram import types


def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Регистрация")
    btn2 = types.KeyboardButton("Посмотреть участников")
    btn3 = types.KeyboardButton("Расписание")
    menu.add(btn1, btn2, btn3)

    return menu


def lets_go():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поехали")
    menu.add(btn1)

    return menu   


def show_username(username):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(username)
    menu.add(btn1)

    return menu


# def yes_no():
#     menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
#     btn1 = types.KeyboardButton("Верно")
#     btn2 = types.KeyboardButton("Исправить")
#     menu.add(btn1, btn2)

#     return menu


def show_contact():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn2 = types.KeyboardButton("Загрузить", request_contact=True)
    btn3 = types.KeyboardButton("Пропустить")
    menu.add(btn2, btn3)

    return menu


def skip():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Пропустить")
    menu.add(btn1)

    return menu