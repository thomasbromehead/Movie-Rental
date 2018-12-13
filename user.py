class User():
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return self.name

    def watched_movies(self):
        #Filter returns a filter object, turn it into a list
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched

