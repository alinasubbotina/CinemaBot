from datetime import datetime
from functions_api import get_films_data, get_showtime
from other_functions import cinemas_and_showtime

try:
    date = str(datetime.now().isoformat())
    films_by_id, films = get_films_data(date)
    print(films)
    location = "51.510391;-0.13013"
    film = input("Enter film name: ")

    text = cinemas_and_showtime(get_showtime(films_by_id[film], date, location))
    print(text)
except KeyError:
    print("Please check API-key")
