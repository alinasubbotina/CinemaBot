import requests
import json


def get_data(date):
    res = requests.get("https://api-gate2.movieglu.com/filmsNowShowing/?n=25&query=odeon+cinemas",
                       headers={
                           "api-version": "v200",
                           "Authorization": "Basic VEVMRTpFQ1RZOTExc1BFWUo=",
                           "x-api-key": "vwcrurVcnk8xm71uDtPhv9vfcuHsg4Jw2sKzSs3w",
                           "client": "TELE",
                           "territory": "UK",
                           "device-datetime": date
                       })
    info = json.loads(res.text)['films']
    data = {}
    for i in range(len(info)):
        data[info[i]['film_name']] = str(info[i]['film_id'])
    return data


date = input("Enter date in format YYYY-MM-DD: ")


def get_showtimes(film, date):
    res = requests.get(f"https://api-gate2.movieglu.com/filmShowTimes/?film_id={get_data(date)[film]}&date={date}",
                       headers={
                           "api-version": "v200",
                           "Authorization": "Basic VEVMRTpFQ1RZOTExc1BFWUo=",
                           "x-api-key": "vwcrurVcnk8xm71uDtPhv9vfcuHsg4Jw2sKzSs3w",
                           "client": "TELE",
                           "territory": "UK",
                           "geolocation": "51.510391;-0.13013",
                           "device-datetime": "2019-06-02T19:30:50.360Z"
                       })
    information = json.loads(res.text)['cinemas']
    data = []
    for cinema in information:
        cinema_info = {}
        cinema_info['cinema_name'] = cinema['cinema_name']
        cinema_info['distance'] = cinema['distance']
        cinema_info['showings'] = {}
        for type in cinema['showings']:
            timetable = cinema['showings'][type]['times']
            list_of_shows = []
            for showtime in timetable:
                list_of_shows.append(showtime['start_time'])
            cinema_info['showings'][type] = list_of_shows
        data.append(cinema_info)
    print(data)
    pass


get_showtimes('Aladdin', date)

