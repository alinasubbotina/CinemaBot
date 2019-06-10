import telebot


def keyboard_films(data):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    for film in data:
        keyboard.row(film)
        film1 = film
    return keyboard, film1


def keyboard_loc():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    button_geo = telebot.types.KeyboardButton(text="Send location", request_location=True)
    button_cancel = telebot.types.KeyboardButton(text="Cancel")

    keyboard.row(button_geo, button_cancel)
    return keyboard
