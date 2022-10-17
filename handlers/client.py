from aiogram import types, Dispatcher
from create_bot_run import bot
from keyboards import kb_client
from data_base import sqlite_db


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом в ЛС, напишите ему:\nhttps://t.me/sushi_sheff_bot')


async def sushi_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


async def sushi_location_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Рбыная 15А')

async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(sushi_open_command, commands=['Режим_работы'])
    dp.register_message_handler(sushi_location_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
