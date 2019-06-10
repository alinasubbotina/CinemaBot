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


def film_buttons(data):
    new_data = []
    for film in data:
        new_data.append(film)
    films1 = []
    films2 = []
    i = 0
    while i < len(new_data) // 2:
        films1.append([new_data[i], new_data[i + 1]])
        i += 2
    films1.append(["Next page"])
    while i < len(new_data):
        films2.append([new_data[i], new_data[i + 1]])
        i += 2
    films2.append(['Previous page'])
    return films1, films2






