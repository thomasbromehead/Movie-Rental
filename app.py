from movie import Movie
from user import User

my_movie = Movie("The Matrix", "sci-fi", False)
user = User("Tom")
user.add_movie("Dumb and Dumber", "comedy", False)
user.add_movie("J", "comedy", False)
user.movies[0].toggle_watched()
print(user.watched_movies())
user.delete_movie("J")
print(user.movies)


