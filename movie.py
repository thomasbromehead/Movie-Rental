class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.director = "Einstein"
        self.watched = watched

    def __repr__(self):
        return self.name

    def toggle_watched(self):
        self.watched = not self.watched

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }