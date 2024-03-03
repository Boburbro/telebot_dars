from telebot import TeleBot
from telebot.types import Message

from tran import local_translator

bot = TeleBot("6736723597:AAElQF73z3lMjIMXmV1dGGj_09tX3QkU1kk")

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Assalomu alaykum")

@bot.message_handler()
def run(message: Message):
    msg = bot.send_message(chat_id=message.chat.id, text="Tarjima qilinmoqda...")
    text = message.text
    tr_text = local_translator(text)
    bot.reply_to(message, tr_text)
    bot.delete_message(message.chat.id, msg.message_id)

bot.infinity_polling()