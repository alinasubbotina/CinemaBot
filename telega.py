import telebot
from check import keys_find, print_text
TOKEN = '849723524:AAFpHeCFklzhkiXyEP5uQHlxm1hJFD9c7eo'
bot = telebot.TeleBot(TOKEN)


def keyboard_films(data):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    for film in data:
        keyboard.row(film)
    return keyboard


keys = keys_find()
keyboard_1 = keyboard_films(keys)
location = {}
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
    try:
        a = keys[message.text]
        try:
            bot.send_message(message.from_user.id, print_text(keys, message.text, location['message.chat.id']))
        except NameError:
            bot.send_message(message.chat.id, 'Please, click on the button below to share your location!'
                                              ' If you want to use another location,'
                                              ' just click on the clip bellow and use the map', reply_markup=keyboard2)
    except KeyError:
        bot.send_message(message.from_user.id, "Hello! I will help you find the nearest sessions to you. "
                                               "Firstly, share your location, and only then choose a film. "
                                               "Just follow my instructions: enter /start")


@bot.message_handler(content_types=['location'])
def get_film(message):
    print(message.text)
    lon = str(message.location.longitude)
    lat = str(message.location.latitude)
    location['message.chat.id'] = lon + ';' + lat
    bot.send_message(message.chat.id, "Great! Now, please, choose a film "
                                      "you would like to watch from a list:", reply_markup=keyboard_1)


bot.polling(none_stop=True)
