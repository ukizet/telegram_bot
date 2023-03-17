from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

upload_button = KeyboardButton('Завантажити піцу')
delete_button = KeyboardButton('Видалити піцу')
back_button = KeyboardButton('Повернутися назад')

admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_kb.add(upload_button).add(delete_button).add(back_button)

