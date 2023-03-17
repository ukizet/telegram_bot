from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

from create_bot import dp
from keyboards import client_kb, admin_kb
from database import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await message.answer('Виберіть потрібний розділ нижче👇', reply_markup=client_kb)

# @dp.message_handler(commands=['WhenWeWork'])
async def when_we_work_command(message : types.Message):
    await message.answer('з 08:00 до 20:00')

async def menu_command(message : types.Message):
    await sqlite_db.sql_read(message=message)
    pass

inline_kb = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton(text='Посилання', callback_data='lore'))\
    .add(InlineKeyboardButton(text='Посилання2', url='https://www.youtube.com/'))\
    .add(InlineKeyboardButton(text='Посилання3', url='https://www.youtube.com/'))\
    .add(InlineKeyboardButton(text='Посилання4', url='https://www.youtube.com/'))\
    .add(InlineKeyboardButton(text='Посилання5', url='https://www.youtube.com/'))\
    .row(InlineKeyboardButton(text='<--', url='https://www.youtube.com/'),\
        InlineKeyboardButton(text='1/5', url='https://www.youtube.com/'),\
        InlineKeyboardButton(text='-->', url='https://www.youtube.com/'))

async def test(message : types.Message):
    await message.answer('test', reply_markup=inline_kb)

async def lore_handler(callback : types.CallbackQuery):
    # print('lore_handler')
    await callback.answer('inline but')

async def return_admin_kb(message : types.Message):
    await message.answer(reply_markup=admin_kb, text='admin')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_start, Text(equals='Старт'))
    dp.register_message_handler(return_admin_kb, Text(equals='Панель адміна'))
    dp.register_message_handler(when_we_work_command, Text(equals='Графік роботи'))
    dp.register_message_handler(menu_command, Text(equals='Меню'))
    dp.register_message_handler(test, Text(equals='test'))
    
    dp.register_callback_query_handler(lore_handler, text='lore')
    
    dp.register_message_handler(command_start)