import requests
import json
from datetime import datetime

NUMBER_OF_FILMS = 15
API_KEY = "fi4EMsF3YRax0duZ4VgJk6NqVcpTtVYM"
DISTANCE = '30'


def get_films_data():
    res = requests.get("https://api.internationalshowtimes.com/v4/movies/",
                       headers={
                           "X-API-Key": API_KEY,
                       },
                       params={
                           'countries': 'GB'
                       })
    if res.status_code == 200:
        info = json.loads(res.text)['movies']
        data = {}
        i = 0
        while i < NUMBER_OF_FILMS:
            data[info[i]['title']] = info[i]['id']
            i += 1
        return data
    else:
        print("Some error happened:", res.status_code)


def get_showtime_id(film_id, location):
    res = requests.get("https://api.internationalshowtimes.com/v4/showtimes?",
                       headers={
                            "X-API-Key": API_KEY
                       },
                       params={
                            "movie_id": film_id,
                            "location": location,
                            "distance": DISTANCE,
                            "time_from": datetime.now()
                       })
    if res.status_code == 200:
        shows = json.loads(res.text)['showtimes']
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
        if res_id.status_code == 200:
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
        else:
            print("Some error happened:", res_id.status_code)
    else:
        print("Some error happened:", res.status_code)


print(get_films_data())
