import requests
import json

USERNAME = "PROJ_5"
API_KEY = "WEzmKYfpMn6biiUg2W0l179dptCad8iA9ozD85zc"
TERRITORY = "UK"
AUTHORIZATION = "Basic UFJPSl81OlBqUm9hb2dEMkRhcg=="


def get_films_data(date):
    res = requests.get("https://api-gate2.movieglu.com/filmsNowShowing/?n=20&query=odeon+cinemas",
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
    for i in range(len(info)):
        data[info[i]['film_name']] = str(info[i]['film_id'])
    return data


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
