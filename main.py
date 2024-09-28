from storage_json import StorageJson  # For JSON storage
from storage_csv import StorageCsv    # For CSV storage
from movie_app import MovieApp

def main():
    # Use your OMDb API key here
    api_key = "71aff867"  # Replace this with your actual API key

    # Choose the storage system, for example, JSON storage
    storage = StorageJson('movies.json')  # or StorageCsv('movies.csv')

    #storage = StorageCsv('movies.csv') # activate for using CSV storage
    #storage = StorageJson('movies.json')  # activate for using Json

    # Create the MovieApp instance with the storage and API key
    movie_app = MovieApp(storage, api_key)
    movie_app.run()


if __name__ == "__main__":
    main()
