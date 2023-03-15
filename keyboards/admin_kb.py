from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

upload_button = KeyboardButton('/Upload_pizza')
delete_button = KeyboardButton('/Delete_pizza')

admin_keyb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyb.add(upload_button).add(delete_button)

