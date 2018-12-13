from movie import Movie
from user import User

user = User("Tom")

user.add_movie("The Matrix", "sci-fi", False)
user.add_movie("Dumb and Dumber", "comedy", False)

user.save_to_file()