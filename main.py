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
    item2 = types.KeyboardButton("Русский язык")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'тест1', reply_markup=markup)


@bot.message_handler(commands=['ege'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите предмет:')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Профильная математика")
    item2 = types.KeyboardButton("Базовая математика")
    item3 = types.KeyboardButton("Русский язык")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'тест2', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.lower() == "огэ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Математика")
        item2 = types.KeyboardButton("Русский язык")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)
        if message.text.lower() == "Русский язык":
            con = sqlite3.connect('db/oge.db')
            cur = con.cursor()
            result = cur.execute("""SELECT task, answer FROM rus_yaz
             WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
            for elem in result:
                print(elem[1])
                bot.send_message(message.chat.id, f'{elem[1]}')

            con.close()

    elif message.text.lower() == "егэ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Профильная математика")
        item2 = types.KeyboardButton("Базовая математика")
        item3 = types.KeyboardButton("Русский язык")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)


bot.infinity_polling()