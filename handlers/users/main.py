from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db
from states.bundle import Registration


# ---Start---
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user
    user_in_db = await db.get_user(user.id)

    print(user_in_db)


    if not user_in_db:
        await message.answer(f"Давай заполним твой профиль? Твоё имя {message.from_user.first_name}",
            reply_markup=keyboard_buttons.yes_no()
        )
        await Registration.name.set()
    
    else:
        await message.answer(f"Привет {user_in_db.name}!", reply_markup=keyboard_buttons.main_menu())


# ---Регистрация---
@dp.message_handler(text="Регистрация", state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user
    user_in_db = await db.get_user(user.id)

    if user_in_db:
        name = user_in_db.name
    
    else:
        name = message.from_user.first_name

    await message.answer(f"Давай заполним твой профиль? Твоё имя {name}",
        reply_markup=keyboard_buttons.yes_no()
    )

    await Registration.name.set()


# ---Посмотреть участников---
@dp.message_handler(text="Посмотреть участников", state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()

    user = message.from_user
    users = await db.get_all_users()

    async with state.proxy() as data:
        data['page'] = 0

    if users:
        user = users[0]
        await message.answer_photo(
            photo = user.photo,
            caption  =  f"Имя: {user.name}\n"
                        f"Номер телефона: {user.phone_number}\n"
                        # f"Город: {user.town}\n"
                        f"Сфера бизнеса: {user.sphere}\n"
                        f"Сайт компании: {user.site}\n"
                        f"Ссылка на Instagram: {user.instagram}\n"
                        f"Ссылка на Facebook: {user.facebook}\n"
                        f"Ссылка на Linkedin: {user.linkedin}\n"
                        f"Хобби: {user.hobby}",
            reply_markup=inline_buttons.pagination()
        )

    else:
        await message.answer("Ничего не найдено")


@dp.message_handler(text='Расписание', state='*')
async def photo(message: types.Message, state: FSMContext):
    await message.answer_photo('AgACAgIAAxkBAAIRjWSVcMYasC9msoB4Mc9JUOpzEDadAAIVzDEbpgpYSNkfgTA_IG4lAQADAgADeQADLwQ')


# @dp.message_handler(content_types='photo')
# async def photo(message: types.Message):
#     print(message.photo[-1].file_id)