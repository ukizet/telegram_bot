from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_button = KeyboardButton('/start')
whenWeWork_button = KeyboardButton('/WhenWeWork')
admin_button = KeyboardButton('/Admin')
menu_button = KeyboardButton('/menu')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(start_button).add(whenWeWork_button).add(admin_button).add(menu_button)