import telebot
from other_functions import cinemas_and_showtime, keyboard_films, keyboard_loc
from functions_api import get_films_data, get_showtime_id
TOKEN = '849723524:AAFpHeCFklzhkiXyEP5uQHlxm1hJFD9c7eo'
bot = telebot.TeleBot(TOKEN)


keys = get_films_data()
keyboard_1, film = keyboard_films(keys)
location = {}
keyboard2 = keyboard_loc()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Awesome! Just click on the button below to share your location!'
                                      ' If you want to use another location,'
                                      ' just click on the clip bellow and use the map', reply_markup=keyboard2)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text != 'Cancel':
        try:
            film_id = keys[message.text]
            try:
                loc = location[message.chat.id]
                showtime = get_showtime_id(film_id, loc)
                text = cinemas_and_showtime(showtime)
                bot.send_message(message.from_user.id, text)
            except KeyError:
                bot.send_message(message.chat.id, 'Please, click on the button below and share your location'
                                              'and then choose a film. '
                                              'Make sure you are in Great Britain.', reply_markup=keyboard2)
        except KeyError or NameError:
            bot.send_message(message.from_user.id, "Hello! I will help you find the nearest sessions to you. "
                                               "Firstly, share your location, and only then choose a film. "
                                               "Just follow my instructions: enter /start")


@bot.message_handler(content_types=['location'])
def get_film(message):
    lon = str(message.location.longitude)
    lat = str(message.location.latitude)
    location[message.chat.id] = lat + ',' + lon
    film_id = keys[film]
    loc = location[message.chat.id]
    showtime = get_showtime_id(film_id, loc)
    text = cinemas_and_showtime(showtime)
    if text == '':
        bot.send_message(message.chat.id, 'Please, click on the button below and share your location'
                                          'once again. '
                                          'Make sure you are in Great Britain.', reply_markup=keyboard2)
    else:
        bot.send_message(message.chat.id, "Great! Now, please, choose a film "
                                          "you would like to watch from a list:", reply_markup=keyboard_1)


bot.polling(none_stop=True)
