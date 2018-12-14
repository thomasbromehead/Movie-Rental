from movie import Movie
from user import User
import os
import json


def menu():
    # Ask for the user's name
    name = input('Enter your name: ')
    # Check if a file exists for that user
    filename = "{}.txt".format(name)
    if file_exists(filename):
        print('file exists')
        with open(filename, 'r') as f:
            json_data = json.load(f)
            user = User.json_load(json_data)
    else:
        user = User(name)

    # If it already exists, welcome them and load their data
    # If not, create a User object

    # Give them a list of options
        # Add a movie
        # See list of movies
            # Set a movie as watched
            # Delete a movie by name
        # See list of watched movies
        # Save and quit

    user_input = input('Enter \'a\' to add a movie, \'w\' to set a movie as \'watched\', \'l\' to list movies'
                       '\'s\' to see the list of watched movies, \'f\' to save '
                       '\'d\' to delete a movie or \'q\' to quit')
    while user_input != 'q':
        if user_input == "a":
            movie_name = input('Enter a name for the movie : \n')
            movie_genre = input('Enter a genre for the movie: \n')
            user.add_movie(movie_name, movie_genre, False)
        elif user_input == "w":
            movie_name = input('Enter the name of the movie to set as watched: \n')
            user.set_watched(movie_name)
        elif user_input == "l":
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == "d":
            movie_name = input('Enter the name of the movie to delete: \n')
            user.delete_movie(movie_name)
        elif user_input == "s":
            for movie in user.watched_movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == "f":
            with open(filename,"a") as f:
                if file_exists(filename):
                    print('file exists')
                    json.dump(user.to_json_existing(), f)
                else:
                    json.dump(user.to_json(), f)


        user_input = input('Enter \'a\' to add a movie, \'w\' to set a movie as \'watched\', \'l\' to list movies'
                           '\'s\' to see the list of movies, \'f\' to save '
                           '\'d\' to delete a movie or \'q\' to quit')

def file_exists(filename):
        return os.path.isfile(filename)

menu()