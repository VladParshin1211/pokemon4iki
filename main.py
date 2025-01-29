import telebot
from telebot import types

TOKEN = '7717324098:AAHGMpE7FeiMlbo9ntqiTByO3BTojGoqlqY'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.send_message(m.chat.id, 'Привет, человек!')
    bot.register_next_step_handler(msg, photo)


def photo(m):
    file = open('C:\ds', 'rb')
    bot.send_photo(m.chat.id, file)
    bot.register_next_step_handler(start)

bot.infinity_polling(True)
#123