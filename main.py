import telebot
import sqlite3
from random import randint
from telebot import types
con1 = sqlite3.connect('db/oge.db')
cur1 = con1.cursor()
token = '5282834057:AAGKZQR5A4HWvcE-oRr15Ucv_OPo2KCVdRA'
bot = telebot.TeleBot(token)
num = randint(1, 5)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ОГЭ")
    item2 = types.KeyboardButton("ЕГЭ")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите, к чему вы хотите готовиться:', reply_markup=markup)


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
            result = cur1.execute(f"SELECT task, answer FROM rus_yaz WHERE id = {num}").fetchall()
            for elem in result:
                bot.send_message(message.chat.id, elem[0])
            con1.close()

    elif message.text.lower() == "егэ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Профильная математика")
        item2 = types.KeyboardButton("Базовая математика")
        item3 = types.KeyboardButton("Русский язык")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, повторите еще раз")


bot.infinity_polling()
