from movie import Movie
import json


class User():
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return self.name

    def watched_movies(self):
        #Filter returns a filter object, turn it into a list
        return list(filter(lambda movie: movie.watched, self.movies))


    def add_movie(self, name, genre, watched):
        movie = Movie(name, genre, watched)
        self.movies.append(movie)

    def delete_movie(self, name: object) -> object:
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name ==  name:
                movie.toggle_watched()

    def save_to_file(self):
        with open('my_file.csv', 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))

    #@classmethod this delimitates class methods, everything underneath is one.

    #def load_from_file(cls, filename):
    #    with open(filename, 'r') as f:
    #       content = f.readlines()
    #        username = content[0]
    #        movies = []
    #        for line in content[1:]:
    #            movie_data = line.split(',') # ["name", "genre", "watched" which should be a boolean not a string ]
    #            movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
    #        user = cls(username)
    #        user.movies = movies
    #        return user

    def to_json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }
    def to_json_existing(self):
        return {
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def json_load(cls, json_data):
        user = cls(json_data['name'])
        movies = []
        for movie in json_data["movies"]:
            movies.append(Movie.json_load(movie))
        user.movies = movies
        return user

