from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.callback_query_handler(text_contains='back')
async def queryFunc(c: types.CallbackQuery, state: FSMContext):
    users = await db.get_all_users()

    async with state.proxy() as data:
        if data['page'] > 0:
            data['page'] -= 1
        elif data['page'] == 0:
            await c.answer("Это первая страница")
            
        page_num = data['page']
    
    print(page_num)
    await c.answer()

    user = users[page_num]
    await c.message.edit_media(
        media = types.InputMedia(
            media = user.photo,
            caption  =  f"Имя: {user.name}\n"
                        f"Номер телефона: {user.phone_number}\n"
                        f"Ссылка на Telegram: {user.username}\n"
                        f"Кратко о себе: {user.about}\n"
                        f"Город: {user.family}\n"
                        f"Хобби: {user.hobby}\n"
                        f"Дополнительно: {user.additional}\n",           
            ),
        reply_markup=inline_buttons.pagination()
    )


@dp.callback_query_handler(text_contains='next')
async def queryFunc(c: types.CallbackQuery, state: FSMContext):
    users = await db.get_all_users()

    async with state.proxy() as data:
        if data['page'] < (len(users) - 1):
            data['page'] += 1
        
        else:
            await c.answer("Это последняя страница")
        page_num = data['page']

    await c.answer()

    user = users[page_num]
    await c.message.edit_media(
        media = types.InputMedia(
            media = user.photo,
            caption  =  f"Имя: {user.name}\n"
                        f"Номер телефона: {user.phone_number}\n"
                        f"Ссылка на Telegram: {user.username}\n"
                        f"Кратко о себе: {user.about}\n"
                        f"Город: {user.family}\n"
                        f"Хобби: {user.hobby}\n"
                        f"Дополнительно: {user.additional}\n",          
            ),
        reply_markup=inline_buttons.pagination()
    )