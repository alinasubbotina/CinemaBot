from datetime import datetime
import telebot


def cinemas_and_showtime(showtime):
    text = ''
    for cinema in showtime:
        date = cinema['start_at'][:10]
        time = cinema['start_at'][11:16]
        day = datetime.strptime(date, '%Y-%m-%d').strftime("%d %B %Y")
        text += f'Cinema {cinema["name"]}\n' \
            f'Address: {cinema["address"]}\n' \
            f'Telephone: {cinema["telephone"]}\n' \
            f'Time of the next session: {time}\n' \
            f'Date: {day}\n' \
            f'Booking link: {cinema["booking_link"]}\n\n'
    return text


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





