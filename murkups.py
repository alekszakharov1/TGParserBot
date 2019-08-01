from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Лучшие')
source_markup_btn2 = types.KeyboardButton('Всё подряд')
source_markup.add(source_markup_btn1, source_markup_btn2)

age_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
age_markup_btn1 =  types.KeyboardButton('Сутки')
age_markup_btn2 =  types.KeyboardButton('неделя')
age_markup_btn3 =  types.KeyboardButton('Месяц')
age_markup.add(age_markup_btn1, age_markup_btn2, age_markup_btn3)

rating_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
rating_markup_btn1 =  types.KeyboardButton('Без порога')
rating_markup_btn2 =  types.KeyboardButton('10')
rating_markup_btn3 =  types.KeyboardButton('25')
rating_markup_btn4 =  types.KeyboardButton('50')
rating_markup_btn5 =  types.KeyboardButton('100')
rating_markup.row(rating_markup_btn1, rating_markup_btn2)
rating_markup.row(rating_markup_btn3, rating_markup_btn4, rating_markup_btn5)

amount_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
amount_markup_btn1 =  types.KeyboardButton('1')
amount_markup_btn2 =  types.KeyboardButton('3')
amount_markup_btn3 =  types.KeyboardButton('5')
amount_markup.add(amount_markup_btn1, amount_markup_btn2, amount_markup_btn3)