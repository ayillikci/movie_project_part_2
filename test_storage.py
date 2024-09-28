from storage_json import StorageJson

# Initialize storage for John
storage = StorageJson('john.json')

# 1. List all movies (should be empty initially)
print("Initial movie list:", storage.list_movies())

# 2. Add a new movie
storage.add_movie("Inception", 2010, 8.8, "https://example.com/poster/inception.jpg")
storage.add_movie("The Matrix", 1999, 8.7)

# 3. List all movies again (after adding)
print("Movie list after adding two movies:", storage.list_movies())

# 4. Update a movie's rating
storage.update_movie("Inception", 9.0)

# 5. List movies to verify the update
print("Movie list after updating Inception's rating:", storage.list_movies())

# 6. Delete a movie
storage.delete_movie("The Matrix")

# 7. List movies after deletion
print("Movie list after deleting The Matrix:", storage.list_movies())
