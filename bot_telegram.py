from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from database import sqlite_db

async def on_startup(_):
    print('Bot is online')
    sqlite_db.sql_start()

def main():
    client.register_handlers_client(dp)
    admin.register_handlers_admin(dp)
    other.register_handlers_other(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    pass

# Запуск бота
if __name__ == '__main__':
    main()
