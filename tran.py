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