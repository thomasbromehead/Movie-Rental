class User():
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return self.name

    def watched_movies(self):
        watched_list = []
        for movie in self.movies:
            if movie.watched == True:
                watched_list.append(movie)
                return watched_list
        return 'No movies watched yet'

