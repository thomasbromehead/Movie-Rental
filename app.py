from movie import Movie
from user import User
import json



#with open('json.txt', 'r') as f:
#json.dump(user.json_dump(), f)


with open('json.txt', 'r') as f:
    json_data = json.load(f)
    user = User.json_load(json_data)
    print(user)
    print(user.movies)
