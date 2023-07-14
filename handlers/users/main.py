from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db
from data.config import PHOTO_FILE_ID
from states.bundle import Registration


# ---Start---
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user
    user_in_db = await db.get_user(user.id)

    if not user_in_db:
        await message.answer(
            "Привет! Мы создаем карточки с интро и фото участников, чтобы было проще и удобнее знакомиться, общаться, а также  находить общие интерсы.\n\n"

            "Поэтому зададим несколько вопросов.  Ответы вместе с фото и контактом - будут сформированы в твою карточку и будут в доступе у других участников клуба.\n"
            "Начнем?",
                reply_markup=keyboard_buttons.lets_go()
        )
    
    else:
        await message.answer(f"Привет {user_in_db.name}!", reply_markup=keyboard_buttons.main_menu())


# ---Регистрация---
@dp.message_handler(text="Регистрация", state='*')
async def registration(message: types.Message, state: FSMContext):
    await message.answer(
        "Привет! Мы создаем карточки с интро и фото участников, чтобы было проще и удобнее знакомиться, общаться, а также  находить общие интерсы.\n\n"

        "Поэтому зададим несколько вопросов.  Ответы вместе с фото и контактом - будут сформированы в твою карточку и будут в доступе у других участников клуба.\n"
        "Начнем?",
            reply_markup=keyboard_buttons.lets_go()
    )


# ---Посмотреть участников---
@dp.message_handler(text="Посмотреть участников", state='*')
async def show_members(message: types.Message, state: FSMContext):
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
                        f"Ссылка на Telegram: {user.username}\n"
                        f"Кратко о себе: {user.about}\n"
                        f"Город: {user.family}\n"
                        f"Хобби: {user.hobby}\n"
                        f"Дополнительно: {user.additional}\n",
            reply_markup=inline_buttons.pagination()
        )

    else:
        await message.answer("Ничего не найдено")


@dp.message_handler(text='Расписание', state='*')
async def schedule(message: types.Message, state: FSMContext):
    await message.answer_photo(PHOTO_FILE_ID)


# @dp.message_handler(content_types='photo')
# async def photo(message: types.Message):
#     print(message.photo[-1].file_id)