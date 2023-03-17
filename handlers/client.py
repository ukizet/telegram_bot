from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import client_kb
from database import sqlite_db
from aiogram.dispatcher.filters import Text

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await message.answer('What do you want?', reply_markup=client_kb)

# @dp.message_handler(commands=['WhenWeWork'])
async def when_we_work_command(message : types.Message):
    await message.answer('з 08:00 до 20:00')

async def menu_command(message : types.Message):
    await sqlite_db.sql_read(message=message)
    pass

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_start, Text(equals='Старт'))
    dp.register_message_handler(when_we_work_command, Text(equals='Графік роботи'))
    dp.register_message_handler(menu_command, Text(equals='Меню'))