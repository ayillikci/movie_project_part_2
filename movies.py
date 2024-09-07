# Copy your code from the previous Movies project
import movie_storage


def input_movie_title():
    movie_title = input("Please enter the movie name: ")
    return movie_title


def input_movie_year():
    while True:
        try:
            movie_year = int(input(f"Please enter the release year: "))
            if movie_year <= 1800 or movie_year > 2025:
                raise ValueError
            break
        except:
            print("Try again")
    return movie_year


def input_movie_rating():
    while True:
        try:
            movie_rating = float(input(f"Please enter a rating 1 to 10: "))
            if movie_rating > 10 or movie_rating < 1:
                raise ValueError
            break
        except:
            print("Try again")
    return movie_rating


def list_movies():
    data = movie_storage.load_movies()
    for item in data.values():
        print(f"Title: {item["title"]}")
        print(f"Year: {item["year"]}")
        print(f"Rating: {item["rating"]}")
        print()
          #  print(f"Movie: {item["title"]} \nReleased Date: {item["year"]} \nRating: {item["rating"]} \n\n")


def add_movie():
    while True:
        title = input_movie_title()
        if movie_storage.movie_exists(title):
            print(f"The movie '{title}' already exists. Please enter a new movie title.")
            continue

        year = input_movie_year()
        rating = input_movie_rating()
        added_movie = movie_storage.add_movie(title,year,rating)
        print(added_movie)
        break


def delete_movie():
    title = input_movie_title()
    deleted_movie = movie_storage.delete_movie(title)
    print (deleted_movie)

def update_movie():
    title = input_movie_title()
    rating = input_movie_rating()
    modified_movie = movie_storage.update_movie(title, rating)
    print (modified_movie)

# Main menu function
def menu():
    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. List movies")
        print("2. Add movie")
        print("3. Remove movie")
        print("4. Update movie\n")

        choice = input("Enter your choice: ")
        print("")
        if choice == '0':
            print("Bye...")
            break
        elif choice == '1':
            #get_movies()
            list_movies()
        elif choice == '2':
            #add_movie()
            add_movie()
        elif choice == '3':
            #delete_movie()
            delete_movie()
        elif choice == '4':
            #update_movie()
            update_movie()
        else:
            print("\nInvalid choice. Please try again.")



def main():
    menu()

if __name__ == "__main__":
    main()