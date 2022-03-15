from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb


async def command_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            'Приветствую в нашей пицерии',
            reply_markup=client_kb,
        )
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:'
                            ' \nhttps://t.me/A4_pizza_bot')


async def command_operating_mode(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Пн-Пт с 10:00 до 20:00, \nСб-Вс с 10:00 до 16:00',
    )


async def command_pizza_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Сырная 4')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_operating_mode, commands=['Режим_работы'])
    dp.register_message_handler(command_pizza_place, commands=['Расположение'])
