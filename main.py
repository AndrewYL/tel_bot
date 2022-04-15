import sqlite3

import telebot
from telebot import types

token = '5282834057:AAGKZQR5A4HWvcE-oRr15Ucv_OPo2KCVdRA'
bot = telebot.TeleBot(token)


# conn1 = sqlite3.connect('db/datab.db', check_same_thread=False)
# cursor1 = conn1.cursor()
# def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, ranswer: int):
# cursor1.execute('INSERT INTO users (user_id, user_name, user_surname, username, ranswer) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, ranswer))
# conn1.commit()
@bot.message_handler(commands=['start'])
def start_message(message):
    # global r
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/oge")
    item2 = types.KeyboardButton("/ege")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите экзамен:', reply_markup=markup)
    # us_id = message.from_user.id
    # us_name = message.from_user.first_name
    # us_sname = message.from_user.last_name
    # username = message.from_user.username
    # db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, ranswer=0)
    # con = sqlite3.connect('db/datab.db')
    # cur = con.cursor()
    # result = cur.execute(f"""SELECT ranswer FROM users
    # WHERE user_id = {message.from_user.id}""").fetchall()
    # for elem in result:
    # r = elem[0]
    # con.close()


@bot.message_handler(commands=['oge'])
def start_message(message):
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
    bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)


@bot.message_handler(commands=['ege'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Профильная математика")
    item2 = types.KeyboardButton("Базовая математика")
    item3 = types.KeyboardButton("Русский язык(ЕГЭ)")
    item4 = types.KeyboardButton("Физика(ЕГЭ)")
    item5 = types.KeyboardButton("Информатика(ЕГЭ)")
    item6 = types.KeyboardButton("Химия(ЕГЭ)")
    item7 = types.KeyboardButton("Биология(ЕГЭ)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    global name
    global correct
    if message.text.lower() == "русский язык(огэ)":
        con = sqlite3.connect('db/oge.db')
        cur = con.cursor()
        name = "Русский язык(ОГЭ)"
        result = cur.execute("""SELECT task, answer FROM rus_yaz
            WHERE id IN (SELECT id FROM rus_yaz ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()
    if message.text.lower() == 'физика(егэ)':
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Физика(ЕГЭ)"
        result = cur.execute("""SELECT task, answer FROM fizika
            WHERE id IN (SELECT id FROM fizika ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()
    if message.text.lower() == 'информатика(егэ)':
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Информатика(ЕГЭ)"
        result = cur.execute("""SELECT task, answer FROM infor
            WHERE id IN (SELECT id FROM infor ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()
    if message.text.lower() == 'химия(егэ)':
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Химия(ЕГЭ)"
        result = cur.execute("""SELECT task, answer FROM him
            WHERE id IN (SELECT id FROM him ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()
    if message.text.lower() == 'биология(егэ)':
        con = sqlite3.connect('db/ege.db')
        cur = con.cursor()
        name = "Биология(ЕГЭ)"
        result = cur.execute("""SELECT task, answer FROM biol
            WHERE id IN (SELECT id FROM biol ORDER BY RANDOM() LIMIT 1)""").fetchall()
        for elem in result:
            print(elem[1])
            correct = elem[1]
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
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
            bot.send_photo(message.chat.id, photo=elem[0])
            bot.send_message(message.from_user.id, 'Ваш ответ:', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_answer)
        con.close()


def get_answer(message):
    global answer
    # global r
    answer = message.text
    if ''.join(answer.lower().split()) == correct:
        # con = sqlite3.connect('db/datab.db')
        # cur = con.cursor()
        # result = cur.execute(f"""UPDATE users
        # SET ranswer = {r}
        # WHERE user_id = {message.from_user.id}""").fetchall()
        # con.commit()
        # con.close()
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
