@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5657862675:AAFMkM1JgH5hWFGYPTiq31wrDEheaBNv5YA

python bot_telegram.py

pause