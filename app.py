from movie import Movie
from user import User
import json

user = User("Thomas")
user.add_movie('The Matrix', "sci-fi", False)
user.add_movie("Dumb and Dumber", "comedy", True)

print(user.json_dump())

with open('json.txt', 'w') as f:
    json.dump(user.json_dump(), f)


