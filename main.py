import telebot
import random

from random import randint

token='6887228444:AAHvWy-WQP0wQIFS6ZCxs6BBusiGkuZPi1k'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'again'])
def start_message(message):
  bot.send_message(message.chat.id,'Я загадал число, попробуйте его угадать!')
  global random_number
  random_number = randint(1, 100)

@bot.message_handler(func=lambda message:True)
def game(message):
  number = int(message.text)
  if random_number == number:
    bot.send_message(message.chat.id, "Да, вы угадали!")
  elif random_number < number:
    bot.send_message(message.chat.id, "Нет. Я загадал число меньше")
  else:
    bot.send_message(message.chat.id, "Нет. Я загадал число больше")

bot.polling()