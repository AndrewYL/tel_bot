import sqlite3
import telebot
from telebot import types
token = '5282834057:AAGKZQR5A4HWvcE-oRr15Ucv_OPo2KCVdRA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/oge")
    item2 = types.KeyboardButton("/ege")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите экзамен:', reply_markup=markup)


@bot.message_handler(commands=['oge'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Математика")
    item2 = types.KeyboardButton("Русский язык(ОГЭ)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)


@bot.message_handler(commands=['ege'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Профильная математика")
    item2 = types.KeyboardButton("Базовая математика")
    item3 = types.KeyboardButton("Русский язык(ЕГЭ)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.lower() == "русский язык(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        global name
        name = "Русский язык(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM rus_yaz
            WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            global correct
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()
    if message.text.lower() == "математика":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Математика"
        result = cur.execute("""SELECT task, answer FROM matem
             WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()


def get_answer(message):
    global answer
    answer = message.text
    if ''.join(answer.lower().split()) == correct:
        bot.send_message(message.chat.id, 'Правильный ответ!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Хотите попробовать еще?', reply_markup=markup)
        bot.register_next_step_handler(message, return0)
    elif ''.join(answer.lower().split()) == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/start")
        markup.add(item)
        bot.send_message(message.chat.id, 'Начнем с начала!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/oge':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/oge")
        markup.add(item)
        bot.send_message(message.chat.id, 'Выберем другой предмет!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/ege':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/ege")
        markup.add(item)
        bot.send_message(message.chat.id, 'Выберем другой предмет!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'К сожалению, это неправильный ответ. Однако у Вас есть возможность '
                                          'попробовать свои силы еще раз')
        bot.register_next_step_handler(message, last_answer)


def last_answer(message):
    global answer
    answer = message.text
    if ''.join(answer.lower().split()) == correct:
        bot.send_message(message.chat.id, 'Правильный ответ!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Хотите попробовать еще?', reply_markup=markup)
        bot.register_next_step_handler(message, return0)
    elif ''.join(answer.lower().split()) == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/start")
        markup.add(item)
        bot.send_message(message.chat.id, 'Начнем с начала!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/oge':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/oge")
        markup.add(item)
        bot.send_message(message.chat.id, 'Выберем другой предмет!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/ege':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/ege")
        markup.add(item)
        bot.send_message(message.chat.id, 'Выберем другой предмет!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'К сожалению, это неправильный ответ')
        bot.send_message(message.chat.id, f'Правильный ответ: {correct}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Хотите попробовать еще?', reply_markup=markup)
        bot.register_next_step_handler(message, return0)


def return0(message):
    com = message.text
    if com.lower() == 'попробовать еще':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton(f"{name}")
        markup.add(item)
        bot.send_message(message.chat.id, 'Начнем с начала', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/start")
        markup.add(item)
        bot.send_message(message.chat.id, 'До скорых встреч!', reply_markup=markup)


bot.infinity_polling()