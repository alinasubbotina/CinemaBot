from datetime import datetime
from functions_api import get_films_data, get_showtime
from other_functions import cinemas_and_showtime, film_buttons
try:
    date = str(datetime.now().isoformat())
    films_by_id = get_films_data(date)
    films_1, films_2 = film_buttons(films_by_id)
    location = "51.510391;-0.13013"
    film = "Aladdin"
    text = cinemas_and_showtime(get_showtime(films_by_id[film], date, location))
except KeyError:
    print("Please check API-key")
