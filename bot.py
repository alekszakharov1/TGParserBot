import bs4
import telebot
import my_parser

from Task import Task
import murkups as m
from bot_token import TOKEN

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# r = requests.get(f'{MAIN_URL}/getMe')
# #
# # print(r.json())

bot = telebot.TeleBot(TOKEN)
task = Task()

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Откуда парсить?', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askSource)
        task.isRunning = True

def askSource(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        task.mySource = 'top'
        msg = bot.send_message(chat_id, 'За какой временной промежуток?', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askAge)
    elif text in task.names[1]:
        task.mySource = 'all'
        msg = bot.send_message(chat_id, 'Какой минимальный порог рейтинга?', reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askRating)
    else:
        msg = bot.send_message(chat_id, 'Такого раздела нет. Введите раздел корректно.')
        bot.register_next_step_handler(msg, askSource)
        return

def askAge(message):
    chat_id = message.chat.id
    text = message.text.lower()
    filters = task.filters[0]
    if text not in filters:
        msg = bot.send_message(chat_id, 'Такого временного промежутка нет. Введите порог корректно.')
        bot.register_next_step_handler(msg, askAge)
        return
    task.myFilter = task.filters_code_names[0][filters.index(text)]
    msg = bot.send_message(chat_id, 'Сколько страниц парсить?', reply_markup=m.amount_markup)
    bot.register_next_step_handler(msg, askAmount)

def askRating(message):
    chat_id = message.chat.id
    text = message.text.lower()
    filters = task.filters[1]
    if text not in filters:
        msg = bot.send_message(chat_id, 'Такого порога нет. Введите порог корректно.')
        bot.register_next_step_handler(msg, askRating)
        return
    task.myFilter = task.filters_code_names[1][filters.index(text)]
    msg = bot.send_message(chat_id, 'Сколько страниц парсить?', reply_markup=m.amount_markup)
    bot.register_next_step_handler(msg, askAmount)

def askAmount(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Количество страниц должно быть числом. Введите корректно.')
        bot.register_next_step_handler(msg, askAmount)
        return
    if int(text) < 1 or int(text) > 5:
        msg = bot.send_message(chat_id, 'Количество страниц должно быть >0 и <6. Введите корректно.')
        bot.register_next_step_handler(msg, askAmount)
        return
    task.isRunning = False
    print(task.mySource + " | " + task.myFilter + ' | ' + text) #
    output = ''
    if task.mySource == 'top':
        output = my_parser.getTitlesFromTop(int(text), task.myFilter)
    else:
        output = my_parser.getTitlesFromAll(int(text), task.myFilter)
    msg = bot.send_message(chat_id, output, reply_markup=m.start_markup)

bot.polling(none_stop=True)
