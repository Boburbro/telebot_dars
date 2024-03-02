<h1 align="center">
  TeleBot
</h1>

## 1-dars

<div align="center">
<iframe 
    src="https://youtu.be/IlsOtPRkyl4?si=WBu2SI1l2XWTOz-V">
</iframe>
</div>

### Telebotni *(pyTelegramBotAPI)* yuklab olish
```pip install PyTelegramBotAPI```

### [1-bot kodi](/birinchiBot.py)

```python
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
```


## 2-dars
### Google tarjimon kutubxonsini yuklab olish
```pip install googletrans==3.1.0a0```

### [Foydalanish:](/tran.py)
```python
from googletrans import Translator

def local_translator(text: str):
    try:
        t = Translator()
        d = t.detect(text).lang
        if d == "en":
            return f"🇺🇿{t.translate(text, str='uz', dest='uz').text}"

        if d == "uz":
            return f"🇬🇧{t.translate(text, str='en', dest='en').text}"
        
        else:
            return "Tarjima qilishda xatolik yuz berdi!"
    except:
        return "Tarjima qilishda xatolik yuz berdi!"
``` 

### [2-bot kodi:](/ikkinchiBot.py)

```python
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
```


