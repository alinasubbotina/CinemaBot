from datetime import datetime


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


def location_type(message, loc):
    lon = str(message.location.longitude)
    lat = str(message.location.latitude)
    loc[message.chat.id] = lat + ',' + lon
    pass
