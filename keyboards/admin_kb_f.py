from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# upload_button = KeyboardButton('Завантажити піцу')
# delete_button = KeyboardButton('Видалити піцу')
# back_button = KeyboardButton('Повернутися назад')

# admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)

# # admin_kb.add(upload_button).add(delete_button).add(back_button)

# admin_kb.row(upload_button, delete_button).row(back_button)

admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(KeyboardButton('Завантажити піцу'), KeyboardButton('Видалити піцу'))\
    .row(KeyboardButton('Повернутися назад'))

download_pizza_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('Відміна'))