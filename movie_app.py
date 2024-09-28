import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

class MovieApp:
    def __init__(self, storage, api_key):
        self._storage = storage
        self._api_key = api_key

    def _command_list_movies(self):
        """List all movies in storage."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return

        for title, details in movies.items():
            print(f"Title: {details['title']}, Year: {details['year']}, Rating: {details['rating']}, Poster URL: {details['poster']}")

    def _command_add_movie(self):
        """Add a movie using the OMDb API."""
        title = input("Enter the movie title: ")
        movie_info = self._fetch_movie_from_omdb(title)

        if movie_info:
            self._storage.add_movie(
                title=movie_info['title'],
                year=movie_info['year'],
                rating=movie_info['rating'],
                poster=movie_info['poster']
            )
            print(f"Movie '{movie_info['title']}' added successfully.")
        else:
            print(f"Failed to add movie '{title}'.")

    def _command_delete_movie(self):
        """Delete a movie by title from the storage."""
        title = input("Enter the title of the movie to delete: ")
        success = self._storage.delete_movie(title)

        if success:
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def _command_update_movie(self):
        """Update the rating of a movie by title."""
        title = input("Enter the title of the movie you want to update: ")
        new_rating = float(input("Enter the new rating: "))

        success = self._storage.update_movie(title, new_rating)

        if success:
            print(f"Movie '{title}' rating updated successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def _command_movie_stats(self):
        """Display statistics such as total movies and average rating."""
        movies = self._storage.list_movies()

        if not movies:
            print("No movies found to calculate statistics.")
            return

        total_movies = len(movies)
        total_rating = sum(movie['rating'] for movie in movies.values())
        average_rating = total_rating / total_movies if total_movies > 0 else 0

        print(f"Total number of movies: {total_movies}")
        print(f"Average movie rating: {average_rating:.2f}")

    def _fetch_movie_from_omdb(self, title):
        """Fetch movie details from the OMDb API."""
        url = f"http://www.omdbapi.com/?apikey={self._api_key}&t={title}"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()
            if data.get('Response') == 'True':
                return {
                    'title': data['Title'],
                    'year': int(data['Year']),
                    'rating': float(data['imdbRating']),
                    'poster': data['Poster']
                }
            else:
                print(f"Movie '{title}' not found in the OMDb database.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect to OMDb API: {e}")
            return None

    def run(self):
        """Display a menu and execute user commands in a loop."""
        while True:
            print("\nMenu:")
            print("1. List movies")
            print("2. Add a movie")
            print("3. Delete a movie")
            print("4. Update a movie's rating")
            print("5. Show movie statistics")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_movie_stats()
            elif choice == "6":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
