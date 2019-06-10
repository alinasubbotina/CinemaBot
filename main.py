from datetime import datetime
from functions_api import get_films_data, get_showtime
from other_functions import cinemas_and_showtime

date = str(datetime.now().isoformat())
films_by_id = get_films_data(date)
for film in films_by_id:
    print(film)

location = "51.510391;-0.13013"
film = input("Enter film name: ")

text = cinemas_and_showtime(get_showtime(films_by_id[film], date, location))
print(text)
