from datetime import datetime


def cinemas_and_showtime(showtime):
    text = ''
    for cinema in showtime:
        day = datetime.strptime(cinema["date"], '%Y-%m-%d').strftime("%d %B %Y")
        if len(cinema['address2']) > 0:
            cinema['address'] += ', ' + cinema['address2']
        text += f'Cinema "{cinema["cinema_name"]}"\n' \
            f'Address: {cinema["address"]}, {cinema["city"]}\n' \
            f'Distance from your location: {round(cinema["distance"], 2)} miles\n' \
            f'Time of the next session: {cinema["time"]}\n' \
            f'Date: {day}.\n\n'
    return text
