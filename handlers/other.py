import json
import string
from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {
        i.lower().translate(str.maketrans('', '', string.punctuation)) for i
        in message.text.split(' ')
    }.intersection(set(json.load(open('stop_list.json')))) != set():
        await message.reply('Мат в чате неприемлем')
        await message.delete()

        # if message.text == 'Привет':
        #     await message.answer('И тебе привет!')
        # await message.reply(message.text)
        # await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
