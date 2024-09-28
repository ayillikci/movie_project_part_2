import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_movies(self):
        """Load the movies from the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_movies(self, movies):
        """Save the movies to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def list_movies(self):
        """List all movies in the storage."""
        return self._load_movies()

    def add_movie(self, title, year, rating, poster=None):
        """Add a new movie to the storage."""
        movies = self._load_movies()
        movies[title] = {
            "title": title,
            "year": year,
            "rating": rating,
            "poster": poster
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        """Delete a movie from the storage."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            return True
        return False

    def update_movie(self, title, rating):
        """Update a movie's rating in the storage."""
        movies = self._load_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)
            return True
        return False
