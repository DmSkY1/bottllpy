import telebot
from telebot import types
import random
from math import *
import pyshorteners
import time
import string
import os
bot_token = os.environ['BOT_TOKEN']
#faunkey = os.environ['FAUNAKEY']
#lmskey = os.environ['LMSKEY']
bot = telebot.TeleBot(bot_token)
commandsbot = '''
/help-список всех команд
/sqrt-квадратный корень числа
/factorial-факториал числа
/random-рандомное число
/short-сокращение ссылки
/randpassword-рандомный пароль
Это бета версия бота, который сделан с образовательной  целью
'''

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))
@bot.message_handler(commands=['start', 'help'])
def wellcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton("/help")
    item2 = types.KeyboardButton("/sqrt")
    item3 = types.KeyboardButton("/factorial")
    item4 = types.KeyboardButton("/random")
    item5 = types.KeyboardButton("/short")
    item6 = types.KeyboardButton("/randpassword")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я {bot.get_me().first_name} вот что я умею' + commandsbot, reply_markup= markup)
@bot.message_handler(commands=['random'])
def randm(message):
    bot.send_message(message.chat.id, f'Держи: {str(random.randint(0, 1000000))}')
@bot.message_handler(commands=['sqrt'])
def sq(message):
    sn = bot.send_message(message.chat.id, 'Введи число:')
    bot.register_next_step_handler(sn, sres)
def sres(message):
    try:
        if int(message.text) > 0:
            bot.send_message(message.chat.id, f'Держи: {sqrt(int(message.text))}')
        else:
            bot.send_message(message.chat.id, 'Простите но квадратный корень не может быть отрицательным')
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный ввод, повторите вызвав команду /sqrt')

@bot.message_handler(commands=['factorial'])
def fact(message):
    s = bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(s, fc)
def fc(message):
    try:
        if int(message.text) > 0:
            bot.send_message(message.chat.id, f'Держи: {factorial(int(message.text))}')
        else:
            bot.send_message(message.chat.id, 'Извините, но факториал должен быть положительным ')
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный ввод, повторите вызвав команду /factorial')
@bot.message_handler(commands=['error24'])
def spam(message):
    for i in range(3):
        time.sleep(5)
        for i in range(50):
            bot.send_message(message.chat.id, 'ERROR')
@bot.message_handler(commands=['randpassword'])
def rand(message):
    bot.send_message(message.chat.id, f'Держи: {randompassword()}')
@bot.message_handler(commands=['short'])
def short(message):
    sn =bot.send_message(message.chat.id, 'Введите ссылку')
    bot.register_next_step_handler(sn, sh)
def sh(message):
    s = pyshorteners.Shortener()
    bot.send_message(message.chat.id, f'Держи: {s.tinyurl.short(message.text)}')

@bot.message_handler(content_types=['text'])
def messif(message):
    if message.text == '/info72':
        bot.send_message(message.chat.id, 'Бота  сделал @demnekron')

bot.polling(none_stop=True)