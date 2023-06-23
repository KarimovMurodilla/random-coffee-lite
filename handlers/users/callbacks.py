from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.callback_query_handler(text_contains='back')
async def queryFunc(c: types.CallbackQuery, state: FSMContext):
    tg_user = c.from_user
    users = await db.get_all_users()

    async with state.proxy() as data:
        if data[tg_user.id]:
            if data[tg_user.id] > 0:
                data[tg_user.id] -= 1
            
        page_num = data[tg_user.id]
    
    user = users[page_num]
    await c.message.edit_media(
        media = types.InputMedia(
            media = user.photo,
            caption  =  f"Имя: {user.name}\n"
                        f"Номер телефона: {user.phone_number}\n"
                        f"Город: {user.town}\n"
                        f"Сфера бизнеса: {user.sphere}\n"
                        f"Сайт компании: {user.site}\n"
                        f"Ссылка на Instagram: {user.instagram}\n"
                        f"Ссылка на Facebook: {user.facebook}\n"
                        f"Ссылка на Linkedin: {user.linkedin}\n"
                        f"Хобби: {user.hobby}",            
            ),
        reply_markup=inline_buttons.pagination()
    )


@dp.callback_query_handler(text_contains='next')
async def queryFunc(c: types.CallbackQuery, state: FSMContext):
    tg_user = c.from_user
    users = await db.get_all_users()

    async with state.proxy() as data:
        if data[tg_user.id] < len(users):
            data[tg_user.id] += 1
            
        page_num = data[tg_user.id]
    
    user = users[page_num]
    await c.message.edit_media(
        media = types.InputMedia(
            media = user.photo,
            caption  =  f"Имя: {user.name}\n"
                        f"Номер телефона: {user.phone_number}\n"
                        f"Город: {user.town}\n"
                        f"Сфера бизнеса: {user.sphere}\n"
                        f"Сайт компании: {user.site}\n"
                        f"Ссылка на Instagram: {user.instagram}\n"
                        f"Ссылка на Facebook: {user.facebook}\n"
                        f"Ссылка на Linkedin: {user.linkedin}\n"
                        f"Хобби: {user.hobby}",            
            ),
        reply_markup=inline_buttons.pagination()
    )