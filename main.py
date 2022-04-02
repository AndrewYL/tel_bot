import sqlite3
import telebot
from telebot import types
token = '5282834057:AAGKZQR5A4HWvcE-oRr15Ucv_OPo2KCVdRA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/oge")
    item2 = types.KeyboardButton("/ege")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите, к чему вы хотите готовиться:', reply_markup=markup)


@bot.message_handler(commands=['oge'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите предмет:')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Математика")
    item2 = types.KeyboardButton("Русский язык(ОГЭ)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'тест1', reply_markup=markup)


@bot.message_handler(commands=['ege'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите предмет:')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Профильная математика")
    item2 = types.KeyboardButton("Базовая математика")
    item3 = types.KeyboardButton("Русский язык(ЕГЭ)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'тест2', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.lower() == "русский язык(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        result = cur.execute("""SELECT task, answer FROM rus_yaz
            WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            global correct
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.register_next_step_handler(message, get_answer)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Хотите попробовать еще?', reply_markup=markup)

        con.close()


def get_answer(message):
    global answer
    answer = message.text
    if answer.lower() == correct:
        bot.send_message(message.chat.id, 'Правильный ответ!')
    else:
        bot.send_message(message.chat.id, 'Ошибка!')


bot.infinity_polling()
