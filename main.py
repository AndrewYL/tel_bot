import os
import sqlite3
from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot.async_telebot import types
users = {}
token = '5282834057:AAGKZQR5A4HWvcE-oRr15Ucv_OPo2KCVdRA'
bot = AsyncTeleBot(token)
conn1 = sqlite3.connect('db/datab.db', check_same_thread=False)
cursor1 = conn1.cursor()


async def db_table_val(user_id: int, ranswer: str):
    cursor1.execute('INSERT INTO users (user_id, ranswer) VALUES (?, ?)', (user_id, ranswer))
    conn1.commit()


@bot.message_handler(commands=['start'])
async def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/oge")
    item2 = types.KeyboardButton("/ege")
    markup.add(item1)
    markup.add(item2)
    await bot.send_message(message.from_user.id, 'Выберите экзамен:', reply_markup=markup)


@bot.message_handler(commands=['oge'])
async def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Математика")
    item2 = types.KeyboardButton("Русский язык(ОГЭ)")
    item3 = types.KeyboardButton("Физика(ОГЭ)")
    item4 = types.KeyboardButton("Информатика(ОГЭ)")
    item5 = types.KeyboardButton("Химия(ОГЭ)")
    item6 = types.KeyboardButton("Биология(ОГЭ)")
    item7 = types.KeyboardButton("География(ОГЭ)")
    item8 = types.KeyboardButton("Обществознание(ОГЭ)")
    item9 = types.KeyboardButton("История(ОГЭ)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    await bot.send_message(message.from_user.id, 'Выберите предмет:', reply_markup=markup)


@bot.message_handler(commands=['ege'])
async def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Профильная математика")
    item2 = types.KeyboardButton("Базовая математика")
    item3 = types.KeyboardButton("Русский язык(ЕГЭ)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    await bot.send_message(message.from_user.id, 'Выберите предмет:', reply_markup=markup)


@bot.message_handler(content_types='text')
async def message_reply(message):
    global id
    global name
    global correct
    message = await message
    idd = message.from_user.id
    if message.text.lower() == "русский язык(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Русский язык(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM rus_yaz
            WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            correct = elem[1]
            users[message.from_user.id] = correct
            await bot.send_photo(message.from_user.id, photo=elem[0])
            print(users)
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "русский язык(егэ)":
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Русский язык(ЕГЭ)"
        result = cur.execute("""SELECT task, answer FROM rus_yaz
            WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(idd, photo=elem[0])
            await bot.send_message(idd, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "профильная математика":
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Профильная математика"
        result = cur.execute("""SELECT task, answer FROM mat_prof
            WHERE id IN (SELECT id FROM mat_prof ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "базовая математика":
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Базовая математика"
        result = cur.execute("""SELECT task, answer FROM mat_baz
            WHERE id IN (SELECT id FROM mat_baz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "математика":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Математика"
        result = cur.execute("""SELECT task, answer FROM matem
             WHERE id IN (SELECT id FROM matem ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "физика(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Физика(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM fizika
             WHERE id IN (SELECT id FROM fizika ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "информатика(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Информатика(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM infor
             WHERE id IN (SELECT id FROM infor ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "химия(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Химия(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM him
             WHERE id IN (SELECT id FROM him ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "биология(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Биология(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM biol
             WHERE id IN (SELECT id FROM biol ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "география(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "География(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM geog
             WHERE id IN (SELECT id FROM geog ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "обществознание(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Обществознание(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM obshes
             WHERE id IN (SELECT id FROM obshes ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()

    if message.text.lower() == "история(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "История(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM hist
             WHERE id IN (SELECT id FROM hist ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            await bot.send_photo(message.from_user.id, photo=elem[0])
            await bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()


async def get_answer(message):
    global answer
    #global r
    answer = message.text
    if ''.join(answer.lower().split()) == correct:
        #con = sqlite3.connect('db/datab.db')
        #cur = con.cursor()
        #result = cur.execute(f"""UPDATE users
        #SET ranswer = {r}
        #WHERE user_id = {message.from_user.id}""").fetchall()
        #con.commit()
        #con.close()
        await bot.send_message(message.from_user.id, 'Правильный ответ!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        await bot.send_message(message.from_user.id, 'Хотите попробовать еще?', reply_markup=markup)
        bot.register_next_step_handler(message, return0)
    elif ''.join(answer.lower().split()) == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/start")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Начнем с начала!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/oge':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/oge")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Выберем другой предмет!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/ege':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/ege")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Выберем другой предмет!', reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id, 'К сожалению, это неправильный ответ. Однако у Вас есть возможность '
                                          'попробовать свои силы еще раз')
        bot.register_next_step_handler(message, last_answer)


async def last_answer(message):
    global answer
    answer = message.text
    if ''.join(answer.lower().split()) == correct:
        await bot.send_message(message.from_user.id, 'Правильный ответ!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        await bot.send_message(message.from_user.id, 'Хотите попробовать еще?', reply_markup=markup)
        bot.register_next_step_handler(message, return0)
    elif ''.join(answer.lower().split()) == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/start")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Начнем с начала!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/oge':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/oge")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Выберем другой предмет!', reply_markup=markup)
    elif ''.join(answer.lower().split()) == '/ege':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/ege")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Выберем другой предмет!', reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id, 'К сожалению, это неправильный ответ')
        await bot.send_message(message.from_user.id, f'Правильный ответ: {correct}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробовать еще")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1)
        markup.add(item2)
        await bot.send_message(message.from_user.id, 'Хотите попробовать еще?', reply_markup=markup)
        bot.register_next_step_handler(message, return0)


async def return0(message):
    com = message.text
    if com.lower() == 'попробовать еще':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton(f"{name}")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'Начнем с начала', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("/start")
        markup.add(item)
        await bot.send_message(message.from_user.id, 'До скорых встреч!', reply_markup=markup)


asyncio.run(bot.polling())