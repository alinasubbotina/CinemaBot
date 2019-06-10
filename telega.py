import telebot
from main import films_1, films_2


telebot.apihelper.proxy = {'https': 'https://35.158.114.186:3128'}

TOKEN = '849723524:AAFpHeCFklzhkiXyEP5uQHlxm1hJFD9c7eo'
bot = telebot.TeleBot(TOKEN)
keyboard_1 = telebot.types.ReplyKeyboardMarkup(films_1)
keyboard_2 = telebot.types.ReplyKeyboardMarkup(films_2)


keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
button_geo = telebot.types.KeyboardButton(text="Send location", request_location=True)
button_cancel = telebot.types.KeyboardButton(text="Cancel")

keyboard2.row(button_geo, button_cancel)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Awesome! Just click on the button below to share your location!'
                                      ' If you want to use another location,'
                                      ' just click on the clip bellow and use the map', reply_markup=keyboard2)


@bot.message_handler(content_types=['text'])
def get_text(message):
        bot.send_message(message.from_user.id, "Hello! Enter /start")


@bot.message_handler(content_types=['location'])
def get_film(message):
    lon = str(message.location.longitude)
    lat = str(message.location.latitude)
    location = lon + ';' + lat
    bot.send_message(message.chat.id, "Please, choose film from a list.", reply_markup=keyboard_1)


bot.polling(none_stop=True)
