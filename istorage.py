from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """List all the movies stored."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Add a new movie."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Delete a movie by title."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Update a movie's rating."""
        pass
