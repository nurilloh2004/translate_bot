from transliteratE import to_cyrillic,to_latin
import Telebot
# TOKEN = '1901094491:AAEPOYQ8jNxxn5L4ELdOteVQ-qBcwhbzWGQ'

TOKEN = '5720178400:AAHDasAcm4uxB1KEgMWCZL94IlD0gqCdDLc'

bot = Telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcom(message):
    javob = "Assalomu alaykum , Xush kelibsiz!"
    javob += "\nMatin kiriting"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()
