import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        """
        Initialize the StorageCsv with the path to the CSV file.
        :param file_path: Path to the CSV file to use for storage.
        """
        self.file_path = file_path

    def _load_movies(self):
        """
        Load movies from the CSV file into a dictionary.
        :return: Dictionary of movies, where the key is the title.
        """
        movies = {}
        try:
            with open(self.file_path, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        'title': title,
                        'year': int(row['year']),
                        'rating': float(row['rating']),
                        'poster': row.get('poster', None)
                    }
        except FileNotFoundError:
            # If the file doesn't exist, return an empty dictionary
            return {}
        return movies

    def _save_movies(self, movies):
        """
        Save the dictionary of movies to the CSV file.
        :param movies: Dictionary of movies to save.
        """
        with open(self.file_path, mode='w', newline='') as f:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for movie in movies.values():
                writer.writerow({
                    'title': movie['title'],
                    'year': movie['year'],
                    'rating': movie['rating'],
                    'poster': movie['poster']
                })

    def list_movies(self):
        """
        List all movies in the storage.
        :return: Dictionary of movies, where the key is the title.
        """
        return self._load_movies()

    def add_movie(self, title, year, rating, poster=None):
        """
        Add a new movie to the storage.
        :param title: Title of the movie.
        :param year: Release year of the movie.
        :param rating: Rating of the movie.
        :param poster: URL of the movie poster (optional).
        """
        movies = self._load_movies()
        movies[title] = {
            'title': title,
            'year': year,
            'rating': rating,
            'poster': poster
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Delete a movie from the storage.
        :param title: Title of the movie to delete.
        :return: True if the movie was deleted, False if not found.
        """
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            return True
        return False

    def update_movie(self, title, rating):
        """
        Update the rating of a movie in the storage.
        :param title: Title of the movie to update.
        :param rating: New rating of the movie.
        :return: True if the movie was updated, False if not found.
        """
        movies = self._load_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)
            return True
        return False
