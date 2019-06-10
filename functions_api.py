import requests
import json

USERNAME = "CINE_27"
API_KEY = "kA7bQzVnm8pPoZpGTFs0axf5XcwYNBY7RTWWYkMb"
TERRITORY = "UK"
AUTHORIZATION = "Basic Q0lORV8yNzpkbEFqc1Q4ajFQa1g="


def get_films_data(date):
    res = requests.get("https://api-gate2.movieglu.com/filmsNowShowing/?n=22&query=odeon+cinemas",
                       headers={
                           "api-version": "v200",
                           "Authorization": AUTHORIZATION,
                           "x-api-key": API_KEY,
                           "client": USERNAME,
                           "territory": TERRITORY,
                           "device-datetime": date
                       })
    info = json.loads(res.text)['films']
    data = {}
    films = []
    for i in range(len(info)):
        films.append(info[i]['film_name'])
        data[info[i]['film_name']] = str(info[i]['film_id'])
    films.insert(11, 'Next page')
    films.insert(23, 'Previous page')
    return data, films


def get_showtime(film_id, datetime, location):
    res = requests.get(f"https://api-gate2.movieglu.com/closestShowing/?",
                       headers={
                           "api-version": "v200",
                           "Authorization": AUTHORIZATION,
                           "x-api-key": API_KEY,
                           "client": USERNAME,
                           "territory": TERRITORY,
                           "geolocation": location,
                           "device-datetime": datetime
                       },
                       params={
                           "film_id": film_id,
                           "date": datetime,
                           "n": '10'
                       })
    data = json.loads(res.text)['cinemas']
    return data
