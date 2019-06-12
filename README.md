# CinemaBot
Telegram Bot for searching showtime

Description:
CinemaBot was created to help you find the closest showtime of movies using your location. 
The bot can provide you with all the available movie sessions only in UK. 
First of all, the bot will request you to share your current location or you can choose it manually, then it checks whether there are any available showtime next to the location that you’ve shared or not. 
Finally, it sends you all the data, from which you can choose.
CinemaBot displays keyboard buttons with the names of films and one button which allows you to share location. 
The bot sends the user all the information using API data from the website(https://www.internationalshowtimes.com/). 
First of all, the program creates a dictionary with the following structure: film -> film id, this is an important step because the search of a movie can be done only with the use of the film id, not the name. 
Then, the program uses the first movie from the list in order to find out whether the user has selected the right location or not. Locations are stored in the dictionary with the structure id chat -> location. 
If the user is located outside of the area that the bot is intended to use, then it will request the user to share location again until he chooses the right spot(in UK). 
Afterwards, when the user selects a movie from the list, the bot will display top 10 closest cinemas, their addresses,  available movies, date and also a link for reservation of tickets. 

Enjoy!!


By Sofia Tretyakova, Alina Subbotina, Daria Chereshneva

