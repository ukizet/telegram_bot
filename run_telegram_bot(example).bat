@echo off

set TOKEN=

cd telegram_bot

cd

call ..\.venv\Scripts\activate.bat

python bot_telegram.py

pause

