from movie import Movie
from user import User

user = User.load_from_file('my_file.csv')
print(user.movies)
