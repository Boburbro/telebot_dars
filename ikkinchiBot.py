from telebot import TeleBot
from telebot.types import Message

from tran import local_translator

bot = TeleBot("6736723597:AAElQF73z3lMjIMXmV1dGGj_09tX3QkU1kk")

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(message.chat.id, "Assalomu alaykum!")


@bot.message_handler()
def run(message: Message):
    text = message.text

    t = local_translator(text)

    bot.reply_to(message, t) 


if __name__ == "__main__":
    bot.infinity_polling()