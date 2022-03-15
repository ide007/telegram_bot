from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

button_1 = KeyboardButton('/Режим_работы')
button_2 = KeyboardButton('/Расположение')
button_3 = KeyboardButton('/Меню')

client_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

client_kb.add(button_1).add(button_2).insert(button_3)
