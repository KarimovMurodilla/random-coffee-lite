import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.bundle import Registration
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


@dp.message_handler(state=Registration.name)
async def process_check_name(message: types.Message, state: FSMContext):
    if message.text == 'Верно':
        async with state.proxy() as data:
            data['name'] = message.from_user.first_name

        profile = await message.from_user.get_profile_photos()

        if profile.photos:
            await message.answer_photo(profile.photos[0][-1].file_id)
            await message.answer("Это твоя фотография?", reply_markup=keyboard_buttons.yes_no())

            async with state.proxy() as data:
                data['photo'] = profile.photos[0][-1].file_id
        else:
            await message.answer("Славно! А теперь отправь фотографию", reply_markup=types.ReplyKeyboardRemove())

        await Registration.next()
    
    elif message.text == 'Исправить':
        await message.answer("Упс, введи своё верное имя")

    else:
        async with state.proxy() as data:
            data['name'] = message.text
        
        profile = await message.from_user.get_profile_photos()

        if profile.photos:
            await message.answer_photo(profile.photos[0][-1].file_id)
            await message.answer("Это твоя фотография?", reply_markup=keyboard_buttons.yes_no())

            async with state.proxy() as data:
                data['photo'] = profile.photos[0][-1].file_id
        else:
            await message.answer("Славно! А теперь отправь фотографию", reply_markup=types.ReplyKeyboardRemove())

        await Registration.next()


@dp.message_handler(content_types=['text', 'photo'], state=Registration.photo)
async def process_photo(message: types.Message, state: FSMContext):
    if message.photo:
        async with state.proxy() as data:
            data['photo'] = message.photo[-1].file_id

        await message.answer("А теперь отправь свой номер телефона", reply_markup=keyboard_buttons.request_contact())
        await Registration.next()

    if message.text == 'Верно':
        await message.answer("А теперь отправь свой номер телефона", reply_markup=keyboard_buttons.request_contact())
        await Registration.next()
    
    elif message.text == 'Исправить':
        await message.answer("Тогда отправь свою фотографию")


@dp.message_handler(content_types=['contact'], state=Registration.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number

    await message.answer("Живешь в Израиле?:", reply_markup = keyboard_buttons.poll())
    await Registration.next()


# @dp.message_handler(state=Registration.town)
# async def process_town(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['town'] = message.text
        
#     await message.answer("Живешь в Израиле?:", reply_markup = keyboard_buttons.poll())
#     await Registration.next()


@dp.message_handler(state=Registration.status_in_israel)
async def process_status_in_israel(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['status_in_israel'] = message.text
        
    await message.answer("Сфера бизнеса", reply_markup=types.ReplyKeyboardRemove())
    await Registration.next()


@dp.message_handler(state=Registration.sphere)
async def process_sphere(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sphere'] = message.text
        
    await message.answer("Сайт компании")
    await Registration.next()


@dp.message_handler(state=Registration.site)
async def process_site(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['site'] = message.text
        
    await message.answer("Ссылка на Instagram", reply_markup=keyboard_buttons.skip())
    await Registration.next()


@dp.message_handler(state=Registration.instagram)
async def process_instagram(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['instagram'] = message.text
        
    await message.answer("Ссылка на Facebook", reply_markup=keyboard_buttons.skip())
    await Registration.next()


@dp.message_handler(state=Registration.facebook)
async def process_facebook(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['facebook'] = message.text
        
    await message.answer("Ссылка на Linkedin", reply_markup=keyboard_buttons.skip())
    await Registration.next()


@dp.message_handler(state=Registration.linkedin)
async def process_linkedin(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['linkedin'] = message.text
        
    await message.answer("Участник сообществ/клубов/бизнес-школ", reply_markup=keyboard_buttons.skip())
    await Registration.next()


@dp.message_handler(state=Registration.member)
async def process_member(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['member'] = message.text
        
    await message.answer("Укажите свое хобби", reply_markup=types.ReplyKeyboardRemove())
    await Registration.next()


@dp.message_handler(state=Registration.hobby)
async def process_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
        
    await message.answer("Твой запрос к участникам клуба")
    await Registration.next()


@dp.message_handler(state=Registration.query)
async def process_query(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['query'] = message.text
        
    await message.answer("Напиши чем можешь помочь участникам клуба")
    await Registration.next()


@dp.message_handler(state=Registration.question)
async def process_question_and_finish(message: types.Message, state: FSMContext):
    user = message.from_user
    async with state.proxy() as data:
        name = data.get('name')
        photo = data.get('photo')
        phone_number = data.get('phone_number')
        town = data.get('town')
        status_in_israel = data.get('status_in_israel')
        sphere = data.get('sphere')
        site = data.get('site')
        instagram = 'Не указано' if data.get('instagram') == 'Пропустить' else data.get('instagram')
        facebook = 'Не указано' if data.get('facebook') == 'Пропустить' else data.get('facebook')
        linkedin = 'Не указано' if data.get('linkedin') == 'Пропустить' else data.get('linkedin')
        member = 'Не указано' if data.get('member') == 'Пропустить' else data.get('member')
        hobby = data.get('hobby')
        query = data.get('query')
        question = message.text
        
    await db.reg_user(
        user_id=user.id,
        username=user.username,
        name=name,
        photo=photo,
        phone_number=phone_number,
        town=town,
        status_in_israel=status_in_israel,
        sphere=sphere,
        site=site,
        instagram=instagram,
        facebook=facebook,
        linkedin=linkedin,
        member=member,
        hobby=hobby,
        query=query,
        question=question
    )

    await message.answer("Ваш профиль успешно создан!", reply_markup=keyboard_buttons.main_menu())
    await state.finish()


