from storage_csv import StorageCsv
from movie_app import MovieApp


def main():
    # Use the StorageCsv class for movie storage in a CSV file
    storage = StorageCsv('movies.csv')

    # Create the MovieApp instance and run it
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()

