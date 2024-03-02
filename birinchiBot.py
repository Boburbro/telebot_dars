import telebot

bot = telebot.TeleBot("6736723597:AAElQF73z3lMjIMXmV1dGGj_09tX3QkU1kk")




@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(chat_id=message.chat.id, text="/start - boshlash\n/help - yordam")

@bot.message_handler(content_types=['text'])
def echo(message):
    if not((message.text).startswith("/")):
        bot.reply_to(message, message.text)
    else:
        bot.reply_to(message, "Bu kamanda!")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Salom!\nBotimizga hush kelibsiz!")


if __name__ == "__main__":
    bot.infinity_polling()
