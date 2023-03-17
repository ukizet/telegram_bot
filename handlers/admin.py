from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from database import sqlite_db
from keyboards import admin_kb, client_kb


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    desc = State()
    price = State()

# Початок діалога завантаження нового пункта(скоріше елемента) меню
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.answer('Give me photo(стискай зображення)')
    pass

async def return_admin_kb(message : types.Message):
    await message.answer(reply_markup=admin_kb, text='admin')

async def return_back_button(message : types.Message):
    await message.answer(reply_markup=client_kb, text='back')
    
# Функція відміни
async def cancel_handler(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

# тут я спробую зробити шаблон всіх цих функцій, так як весь цей код не відповідає DRY
async def load_template(message: types.Message, state: FSMContext, load_type: str, text: str='', finish: bool=False):
    if load_type == 'photo':
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
    else:
        async with state.proxy() as data:
            data[f'{load_type}'] = message.text
    if finish == True:
        async with state.proxy() as data:
            await message.answer(str(data))

        await sqlite_db.sql_add(state=state)
        await state.finish()
    else:
        await FSMAdmin.next()
        if len(text) > 0:
            await message.answer(f'{text}')
        else:
            pass

# Отримуємо першу відповідь від користувача та записуємо її в словник
async def load_photo(message : types.Message, state : FSMContext):
    await load_template(message=message, state=state, load_type='photo', text='Give me name of the pizza')

# Отримуємо другу відповідь від користувача 
async def load_name(message : types.Message, state : FSMContext):
    await load_template(message=message, state=state, load_type='name', text='Give me pizza description')

# Отримуємо третю відповідь від користувача 
async def load_desc(message : types.Message, state : FSMContext):
    await load_template(message=message, state=state, load_type='desc', text='Give me price of the pizza')

# Отримуємо останню відповідь від користувача 
async def load_price(message : types.Message, state : FSMContext, get=None):
    # if get == 'state': return FSMAdmin.price
    await load_template(message=message, state=state, load_type='price', text='', finish=True)

def register_handlers_admin(dp : Dispatcher):
    """
    короче, тут щоб не перечисляти всі ці функції і не реєструвати їх одна за одною можна зробити так: 
    Дати кожному хендлеру якийсь параметр, і зробити тут цикл фор який би перевіряв цей параметр, і потім цей цикл фор реєстрував би кожен хендлер, а всі ці стейти, командси, та контент тайпси
    можна зберігати в самих функціях і потім їх якось підтягувати в цикл при реєстрації
    """
    dp.register_message_handler(cm_start, Text(equals='Завантажити піцу'), state=None)
    dp.register_message_handler(return_admin_kb, Text(equals='Панель адміна'))
    dp.register_message_handler(return_back_button, Text(equals='Повернутися назад'))
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_desc, state=FSMAdmin.desc)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    # dp.register_message_handler(cancel_handler, state=)
    pass
















"""
    # await FSMAdmin.name.set()
    # await message.answer('Give me name of the pizza')
    # await FSMAdmin.desc.set()
    # await message.answer('Give me pizza description')
    # await FSMAdmin.price.set()
    # await message.answer('Give me price of the pizza')

    # async with state.proxy() as data:
    #     data['photo'] = message.photo[0].file_id
    # await FSMAdmin.next()
    # await message.answer('Give me name of the pizza')

    # async with state.proxy() as data:
    #     data['name'] = message.text
    # await FSMAdmin.next()
    # await message.answer('Give me pizza description')

    # async with state.proxy() as data:
    #     data['desc'] = message.text
    # await FSMAdmin.next()
    # await message.answer('Give me price of the pizza')

    # async with state.proxy() as data:
    #     data['price'] = float(message.text)
    # async with state.proxy() as data:
    #     await message.answer(str(data))
    # await state.finish()
"""