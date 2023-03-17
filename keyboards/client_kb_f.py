from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# start_button = KeyboardButton('Старт')
# whenWeWork_button = KeyboardButton('Графік роботи')
# admin_button = KeyboardButton('Панель адміна')
# menu_button = KeyboardButton('Меню')

# client_kb = ReplyKeyboardMarkup(resize_keyboard=True)

# # client_kb.add(start_button).insert(whenWeWork_button).add(admin_button).insert(menu_button)
# client_kb.row(start_button, admin_button).row(whenWeWork_button, menu_button)

client_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(KeyboardButton('Старт'), KeyboardButton('Панель адміна'))\
    .row(KeyboardButton('Графік роботи'), KeyboardButton('Меню'))