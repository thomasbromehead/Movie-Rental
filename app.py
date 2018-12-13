from movie import Movie
from user import User

my_movie = Movie("The Matrix", "sci-fi", False)
user = User("Tom")
user.movies.append(my_movie)
print(user.watched_movies())
user.movies[0].toggle_watched()
print(user.watched_movies())


