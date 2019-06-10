import requests
import json
from datetime import datetime

NUMBER_OF_FILMS = 15
API_KEY = "fi4EMsF3YRax0duZ4VgJk6NqVcpTtVYM"
DISTANCE = '10'


def get_films_data():
    res = requests.get("https://api.internationalshowtimes.com/v4/movies/",
                       headers={
                           "X-API-Key": API_KEY,
                       },
                       params={
                           'countries': 'GB'
                       })
    info = json.loads(res.text)['movies']
    data = {}
    i = 0
    while i < NUMBER_OF_FILMS:
        data[info[i]['title']] = info[i]['id']
        i += 1
    return data


def get_showtime_id(film_id, location):
    res_showtime = requests.get("https://api.internationalshowtimes.com/v4/showtimes?",
                       headers={
                           "X-API-Key": API_KEY
                       },
                       params={
                           "movie_id": film_id,
                           "location": location,
                           "distance": DISTANCE,
                           "time_from": datetime.now()
                       })
    shows = json.loads(res_showtime.text)['showtimes']
    showtime = {}
    for show in shows:
        if show['cinema_id'] not in showtime and len(showtime) < 10:
            showtime[show['cinema_id']] = show
    res_id = requests.get("https://api.internationalshowtimes.com/v4/cinemas/?",
                        headers={
                            "X-API-Key": API_KEY
                        },
                        params={
                            "location": location,
                            "distance": DISTANCE,
                            'countries': 'GB'
                        })
    cinema_id = json.loads(res_id.text)['cinemas']
    data = []
    for session in showtime:
        for cinema in cinema_id:
            if cinema['id'] == session:
                line = {
                    'id': cinema['id'],
                    'name': cinema['name'],
                    'address': cinema['location']['address']['display_text'],
                    'telephone': cinema['telephone'],
                    'start_at': showtime[cinema['id']]['start_at'],
                    'booking_link': showtime[cinema['id']]['booking_link']
                }
                data.append(line)
    return data


print(get_films_data())
