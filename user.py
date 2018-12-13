from movie import Movie


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

