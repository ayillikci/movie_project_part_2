import json
import os
FILE_PATH = "data.json"

# Gets movie database by reading from file.
def load_movies():
    if not os.path.exists(FILE_PATH):
        return {}
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            if not isinstance(data,dict):
                return {}
            return data
    except(json.JSONDecodeError,FileNotFoundError):
        return {}






"""
The Program functions use new_data.json and new_data.
new_data gets loaded by data.json in each program run to 
keep integrity of the movie database(data.json).
"""


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    data = load_movies()
    return data


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("data.json", "w") as file:
        json.dump(movies, file)

def movie_exists(title):

    movies = load_movies()
    title_lower = title.lower()
    for movie_title in movies:
        if title_lower == movie_title.lower():
            return True
    else:
        return False


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # add new movie distionary to existing movie list dictionary
    movies = load_movies()
    movies[title]={
        "title" : title,
        "year" : year,
        "rating" : rating
    }

    save_movies(movies)
    return f"The movie {title} added successfully"

def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = load_movies()
    del movies[title]
    save_movies(movies)
    return f"The {title} has been removed"


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = load_movies()
    movies[title] ["rating"] = rating
    save_movies(movies)
    return f"The movie {title} has been modified"

