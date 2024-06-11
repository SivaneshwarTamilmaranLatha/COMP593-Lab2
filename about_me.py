def main():    
    # Create a complex data structure
    about_me = {
        "full_name": "Sivaneshwar Tamilmaran Latha",
        "student_id": 10330093,
        "pizza_toppings": [
            "CHEESE", 
            "PEPPERONI", 
            "TOMATO SAUCE"
        ],
        "movies": [
            {
                "title": "leo",
                "genre": "action"
            },
            {
                "title": "bigil",
                "genre": "sport"
            }
        ]
    }
    
    # Add another movie to the data structure
    new_movie = {"title": "varisu", "genre": "drama"}
    about_me['movies'].append(new_movie)

    # Function that prints student name and ID
    print_student_name_and_id(about_me)

    # Before adding new pizza toppings, print the pizza toppings
    print_pizza_toppings(about_me)

    # Add new pizza toppings
    add_pizza_toppings(about_me, ("ONIONS", "CAPSICUM"))

    # After adding new pizza toppings, print the pizza toppings
    print_pizza_toppings(about_me)

    # print comma-separated list of movie genres
    print_movie_genres(about_me)

    # print comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

# Function that prints student name and ID
def print_student_name_and_id(about_me):
    first_name = about_me['full_name'].split()[0]
    print(f'My name is {about_me['full_name']}, but you can call Mr. {first_name}.')
    print(f'My student ID is {about_me['student_id']}.')   

# Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'].sort()
    for topping in about_me['pizza_toppings']:
        topping.lower()
    
# Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f'- {topping}')

# Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f'I like to watch {', '.join(genres[:-1])}, and {genres[-1]} movies.')

# Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]
    print(f"Some of my favourite movies are {', '.join(titles[:-1])}, and {titles[-1]}!")

if __name__ == '__main__':
    main()