import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.bundle import Registration
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


@dp.message_handler(text = "Поехали")
async def process_lets_go(message: types.Message, state: FSMContext):
    await message.answer(
        "Представься, пожалуйста",
            reply_markup=types.ReplyKeyboardRemove()
    )
    await Registration.name.set()


@dp.message_handler(state=Registration.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    username = f'@{message.from_user.username}'
    await message.answer("Твой ник в телеграм", reply_markup=keyboard_buttons.show_username(username))
    await Registration.next()


@dp.message_handler(state=Registration.username)
async def process_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text

    await message.answer(
        "Хочешь оставить контактный номер телефона (не обязательно)", 
            reply_markup = keyboard_buttons.show_contact()
        )
    await Registration.next()


@dp.message_handler(content_types=['contact', 'text'], state=Registration.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    if message.contact:
        async with state.proxy() as data:
            phone_number = message.contact.phone_number
            data['phone_number'] = phone_number if phone_number.startswith('+') else f"+{phone_number}"

    if message.text == 'Пропустить':
        async with state.proxy() as data:
            data['phone_number'] = 'Пропустить'

    photo = await message.from_user.get_profile_photos()
    
    await message.answer("Какое фото можно использовать?", reply_markup=keyboard_buttons.photo_choose())
    await message.answer_photo(photo.photos[0][-1].file_id)


    async with state.proxy() as data:
        data['photo'] = photo.photos[0][-1].file_id

    await Registration.next()


@dp.message_handler(content_types=['photo', 'text'], state=Registration.photo)
async def process_photo(message: types.Message, state: FSMContext):
    if message.text:
        if message.text == 'Подтвердить':
            await message.answer(
                "Расскажи кратко о своем бизнесе, чем занимаешься, экспертиза",
                    reply_markup=keyboard_buttons.skip()
                )
            await Registration.next()  

        elif message.text == 'Загрузить':
            await message.answer("Отправь свою фотографию")

    if message.photo:
        async with state.proxy() as data:
            data['photo'] = message.photo[-1].file_id

        await message.answer(
            "Расскажи кратко о своем бизнесе, чем занимаешься, экспертиза",
                reply_markup=keyboard_buttons.skip()
            )
        await Registration.next()


@dp.message_handler(state=Registration.about)
async def process_about(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['about'] = message.text

    await message.answer(
        "Расскажи о семье, где живешь",
            reply_markup=keyboard_buttons.skip()
        )
    await Registration.next()


@dp.message_handler(state=Registration.family)
async def process_family(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['family'] = message.text

    await message.answer(
        "Расскажи кратко об увлечениях, хобби",
            reply_markup=keyboard_buttons.skip()
        )
    await Registration.next()


@dp.message_handler(state=Registration.hobby)
async def process_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text

    await message.answer(
        "Есть что-то еще что хочется добавить?",
            reply_markup=keyboard_buttons.skip()
        )
    await Registration.next()


@dp.message_handler(state=Registration.additional)
async def process_additional_and_finish(message: types.Message, state: FSMContext):
    user = message.from_user

    async with state.proxy() as data:
        name = data.get('name')
        username = data.get('username')
        phone_number = 'Не указано' if data.get('phone_number') == 'Пропустить' else data.get('phone_number')
        photo = data.get('photo')
        about = 'Не указано' if data.get('about') == 'Пропустить' else data.get('about')
        family = 'Не указано' if data.get('family') == 'Пропустить' else data.get('family')
        hobby = 'Не указано' if data.get('hobby') == 'Пропустить' else data.get('hobby')
        additional = 'Не указано' if message.text == 'Пропустить' else message.text
        
    await db.reg_user(
        user_id=user.id,
        name=name,
        username=username,
        phone_number=phone_number,
        photo=photo,
        about=about,
        family=family,
        hobby=hobby,
        additional=additional
    )

    await message.answer("Спасибо и до встречи!", reply_markup=keyboard_buttons.main_menu())
    await state.finish()


