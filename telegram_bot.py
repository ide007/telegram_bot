import json
import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в рабочий режим.')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую в нашей'
                                                     ' пицерии')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:'
                            ' \nhttps://t.me/A4_pizza_bot')


@dp.message_handler(commands=['Режим_работы'])
async def command_operating_mode(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 10:00 до 20:00,'
                                                 '\nСб-Вс с 10:00 до 16:00')


@dp.message_handler(commands=['Расположение'])
async def command_pizza_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Сырная 4')


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i
        in message.text.split(' ')}.intersection(set(json.load(open('stop_list.json')))) != set():
        await message.reply('Мат в чате неприемлем')
        await message.delete()

    # if message.text == 'Привет':
    #     await message.answer('И тебе привет!')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
