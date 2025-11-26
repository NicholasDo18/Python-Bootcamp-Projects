print("Welcome to the Movie Rating System!")
print("Menu:\n1. Add a rating\n2. View average rating of a movie\n3. View all movies and ratings\n4. Quit")

movie_with_ratings = {}

def add_rating(movie_name, rating):
    if movie_name in movie_with_ratings:
        movie_with_ratings[movie_name].append(rating)
    else:
        movie_with_ratings[movie_name] = [rating]

def average_rating(movie_name):
    if movie_name in movie_with_ratings:
        ratings = movie_with_ratings[movie_name]
        avg_rating = sum(ratings) / len(ratings)
        print(f"The average rating for {movie_name} is {avg_rating:.1f}")
    else:
        print("Movie rating not found")

def show_all_movies():
    if movie_with_ratings == {}:
        print("No movies have been added yet.")
    else:
        print("All movies and their average ratings:")
        for key in movie_with_ratings:
            ratings = movie_with_ratings[key]
            avg_rating = sum(ratings) / len(ratings)
            print(f"{key}: {avg_rating:.1f}")

option = int(input("Choose an option (1-4): "))

while True:
    if option == 1:
        movie_name = input("Enter the movie name: ")
        rating = int(input("Enter your rating (1-10): "))
        add_rating(movie_name, rating)
    elif option == 2:
        movie_name = input("Enter the movie name: ")
        average_rating(movie_name)
    elif option == 3:
        show_all_movies()
    elif option == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid option, bye bye")
        break
    
    option = int(input("Choose an option (1-4): "))
