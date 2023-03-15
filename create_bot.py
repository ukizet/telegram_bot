from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

# with open('telegram_bot\TOKEN.txt', 'r') as file:
	# token = file.read()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)