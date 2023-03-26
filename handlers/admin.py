from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import sqlite_db
from keyboards import client_kb, cancel_button


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    desc = State()
    price = State()

# Початок діалога завантаження нового елемента меню
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.answer('Give me photo(стискай зображення)', reply_markup=cancel_button)

async def return_back_button(message : types.Message):
    await message.answer(reply_markup=client_kb, text='back')
    
# Функція відміни
async def cancel_handler(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    print(f'current_state: {current_state}')
    if current_state is None:
        # print(f'current_state: IS NONE!!!')
        return
    await state.finish()
    await message.reply('OK', reply_markup=client_kb)

# тут я спробую зробити шаблон всіх цих функцій, так як весь цей код не відповідає DRY
async def load_template(message: types.Message, state: FSMContext, load_type: str, text: str='', finish: bool=False, test: bool=False):
    async def state_proxy_with_test():
        if test == True:
            return
        return await state.proxy()
    
    if load_type == 'photo':
        async with state_proxy_with_test() as data:
            data['photo'] = message.photo[0].file_id
    else:
        async with state_proxy_with_test() as data:
            data[f'{load_type}'] = message.text
    if finish == True:
        async with state_proxy_with_test() as data:
            await message.answer(str(data), reply_markup=client_kb)

        await sqlite_db.sql_add(state=state)
        await state.finish()
    else:
        """
        ЦЕ ВСЕ НАЇОБ, Я ПРОСТО ДАУН ЯКИЙ НЕ ЗБЕРІГ ФАЙЛ ПІСЛЯ ЗМІН.

        короче тільки що я протестував додавання нового елемента без 'await FSMAdmin.next()' і можу сказати що без нього все працює точно так як і раніше.
        Тобто зараз в цьому 'await FSMAdmin.next()' нема ніякого сенсу. 
        Але їбать, я не розумію чого воно працює, тобто як визиваються ці обробники станів якщо я при їх реєстрації просто передаю стан?

        ЦЕ ВСЕ НАЇОБ, Я ПРОСТО ДАУН ЯКИЙ НЕ ЗБЕРІГ ФАЙЛ ПІСЛЯ ЗМІН.
        """
        await FSMAdmin.next()
        if len(text) > 0:
            await message.answer(f'{text}')
        else:
            pass

# Отримуємо першу відповідь від користувача та записуємо її в словник
async def load_photo(message : types.Message, state : FSMContext):
    # Крч треба спробувати тут відправляти те повідомлення від бота. По типу "завантажте фото"
    # await message.answer(f'Give me photo')
    """
    Не працює через те що цей обробник всього що відбувається в стані фото, 
    не може вивести повідомлення перед тим як користувач відправить фото.
    бо саме відправка фото я запускає цей обробник
    """
    await load_template(message=message, state=state, load_type='photo', text='Give me pizza name')

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
    def register_buttons():
        dp.register_message_handler(cm_start, Text(equals='Завантажити піцу'), state=None)
        dp.register_message_handler(return_back_button, Text(equals='Повернутися назад'))
        dp.register_message_handler(cancel_handler, Text(equals='Відміна'), state="*")

    def register_cm_start_states():
        dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
        dp.register_message_handler(load_name, state=FSMAdmin.name)
        dp.register_message_handler(load_desc, state=FSMAdmin.desc)
        dp.register_message_handler(load_price, state=FSMAdmin.price)
        # dp.register_message_handler(cancel_handler, state=)

    register_buttons()
    register_cm_start_states()

















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
