# Programming by: Tiffany Hodges
# Date: 10/30/2020
# CS223 - Python
# Programming Homework #2 - Movie Library


# function to set a range for the years of movies
# this will be used within the get_movie_info() & edit_movie() functions where user enters a year for the movie
BEGIN_YEAR = 1888
END_YEAR = 2020

def get_year_from_user(prompt, BEGIN_YEAR, END_YEAR):
    while True:
        user_input = input(prompt)
        if not user_input.isdecimal():
            print("The input entered was not an integer. Please try again.")
        else:
            user_int = int(user_input)
            if user_int < BEGIN_YEAR:
                print("Movies did not exist yet. Please try again.")
            elif user_int > END_YEAR:
                print("You cannot enter a year of the future. Please try again.")
            else:
                return user_int


# function to check user's input for a number within certain range
# this is used within the get_movie_info() function where user enters a rating for a new movie
BEGIN_RATING = 1
END_RATING = 5

def get_rating_from_user(prompt, BEGIN_RATING, END_RATING):
    while True:
        user_input = input(prompt)
        if not user_input.isdecimal():
            print("The input entered was not an integer. Please try again.")
        else:
            user_int = int(user_input)
            if user_int < BEGIN_RATING or user_int > END_RATING:
                print("The number entered is out of range. Please try again.")
            else:
                return user_int


# function to check user's input for ONE valid letter
# the valid character can be upper or lower case
# this function is used within the main() function where user needs to select a menu option
# it is also used within the delete_movie() and edit_movie() functions when asked for a yes or no choice
def get_char_from_user(prompt, valid_chars='ladeqLADEQ'):
    while True:
        user_input = input(prompt)
        if len(user_input) != 1:
            print("Please enter only a single letter")
        elif user_input not in valid_chars:
            print("That character is not valid, please try again.")
        else:
            return user_input


# function to check that user is entering a number rather than a letter or other character
# used within the edit_movie() and delete_movie() functions when user is asked to enter index #
BEGIN_INDEX_RANGE = 0
END_INDEX_RANGE = 1000000

def check_for_int(prompt, BEGIN_INDEX_RANGE, END_INDEX_RANGE):
    while True:
        user_input = input(prompt)
        if not user_input.isdecimal():
            print("You have entered an invalid character. Please only enter a number.")
            print()
        else:
            user_int = int(user_input)
            if user_int < BEGIN_INDEX_RANGE or user_int > END_INDEX_RANGE:
                print("The number entered is out of range. Please try again.")
                print()
            else:
                return user_int


# function to print the movies row by row rather than in one long string of text
# takes the inner list of the 2D array and puts it in another list that is more readable
# I do not take credit for this code. I had help from YouTube video: https://www.youtube.com/watch?v=6ZId6BJS7kA 
def list_movies(movie_list):
    if len(movie_list) > 0:
        for inner_list in movie_list:
            if isinstance(inner_list, list):
                for movie in inner_list:
                    print(movie, end=" ") # makes it so there is a space between title, year and rating
                print() # print each movie on new line
    else:
        print("Uh oh! The Movie Library is empty.")


# function to print the index #'s of the movies
# function first checks to be sure there are movies in the list
# used within the edit_movie function. User needs to know the index # of the movie they want to edit
def print_movie_indexes(movie_list):
    if len(movie_list) > 0:
        for movie in range(0, len(movie_list)):
            print("Index #: ", movie, " | Movie: ", movie_list[movie])
        print()
    else:
        print("There is nothing to edit. The Movie Library is empty")


# this function gathers all info of the new movie that user wants to add
# user input for the year and rating will be checked against their corresponding functions
# a new_movie will be returned and passed into the add_movie() function when called
def get_movie_info():
    movie_title = input("Please enter the title of the movie: ")
    movie_year = get_year_from_user("Please enter the year of the movie: ", BEGIN_YEAR, END_YEAR)
    movie_rating = get_rating_from_user("Please enter a rating for the movie between 1 and 5: ", BEGIN_RATING, END_RATING)
    new_movie = [movie_title, movie_year, movie_rating]
    return new_movie


# this function adds the newly created movie, (new_movie), to the END of the list
# since movies will always append/be added to end of list, I confirm with user the movie they added by using -1 index position
# FYI: index 0 is title, 1 is year, and 2 is rating
def add_movie(movie_list):
    movie_list.append(get_movie_info())
    print("You have added '", movie_list[-1][0], "' to the Movie Library.")


# function to edit an existing movie in the list
# will first check to make sure library is not empty, then will print an indexed list of the movies
# user is asked to enter the index # of movie they want to edit
# user input will be checked for a valid character (a number)
# user will be told if they enter a index number that does not exist
# program will confirm with user their choice and whether or not they want to proceed
# if user enters yes, they will be asked to enter the new title, year, and rating for the movie
# if user enters no, they will be taken back to main menu
# in the movie list, 0 element is title, 1 is year, and 2 is rating
# if movie list is empty, they will be taken back to main menu
def edit_movie(movie_list):
    while True:
        if len(movie_list) > 0:
            print_movie_indexes(movie_list)
            movie_to_edit = check_for_int("Please enter the index # of the movie you would like to edit: ", BEGIN_INDEX_RANGE, END_INDEX_RANGE)

            if movie_to_edit in range(0, len(movie_list)):
                edit_decision = get_char_from_user("You are about to edit " + str(movie_list[movie_to_edit][0]) + ". Are you sure? (y/n): ", 'ynYN')
                print()
                if ((edit_decision == "y") or (edit_decision == "Y")): 
                    edited_title = input("Enter the new title: ")
                    movie_list[movie_to_edit][0] = edited_title

                    edited_year = get_year_from_user("Enter the new year: ", BEGIN_YEAR, END_YEAR)
                    movie_list[movie_to_edit][1] = edited_year

                    edited_rating = get_rating_from_user("Enter the new rating: ", BEGIN_RATING, END_RATING)
                    movie_list[movie_to_edit][2] = edited_rating

                    movie_to_edit = [edited_title, edited_year, edited_rating]
                    print(".....Edit successful.....")
                    print()
                    break
                else:
                    print(".....Exiting edit mode.....")
                    break
            else:
                print("That index # does not exist. Please try again.")
                print()
        else:
            print("There is nothing to edit because the Movie Library is empty.")
            break


# function to delete a movie by entering it's index #
# will check to make sure movie list is not empty, then print an indexed list of the movies
# user will be asked to enter the index # of the movie they want to edit
# user's input will be checked to be sure the index # exists
# once user enters a valid index #, user will need to confirm if they want to delete the movie they chose
# if user says yes, movie will be deleted and take suer back to main menu
# if user says no, they will be taken back to main menu 
# if movie list is empty, they will be taken back to main menu
def delete_movie(movie_list):
    while True:
        if len(movie_list) > 0:
            print_movie_indexes(movie_list)
            movie_to_delete = check_for_int("Enter the index # of the movie you would like to delete: ", BEGIN_INDEX_RANGE, END_INDEX_RANGE)
            if movie_to_delete in range(0, len(movie_list)):
                delete_decision = get_char_from_user("Are you sure you want to delete " + str(movie_list[movie_to_delete][0]) + "? (y/n): ", 'ynYN')
                print()
                if ((delete_decision == "y") or (delete_decision == "Y")):
                    print(str(movie_list[movie_to_delete][0]) + " has been deleted.")
                    del movie_list[movie_to_delete]
                    break
                else:
                    print(".....Exiting delete mode.....")
                    break
            else:
                print("That index # does not exist.")
                print()
        else:
            print("There is nothing to delete because the Movie Library is empty.")
            break


# function to print the menu selections
def print_menu():
    print(
        """
        Welcome to the Movie Library

        (L)ist – List all movies
        (A)dd – Add a movie to the list
        (E)dit – Edit a movie on the list
        (D)elete – Delete a movie on the list
        (Q)uit – Exit the program
    
        """
        )


# function to welcome user to the movies library and ask for their selection
# a few movies have been hard-coded in order to put something there rather than an empty list
def main():
    movie_list = [  ["Pulp Fiction", 1994, 4],
                    ["Django", 2012, 5],
                    ["Death Proof", 2007, 5],
                 ]

    user_choice = None

    # main logic loop to get user's choice which will call the corresponding function
    # user must select a valid option or else they will be asked to try again
    # loop will always print the welcome statement with their choices after they have completed each selection all the way through
    # if user decides to quit, the program will stop running and movie list will go back to its original form (3 listings)
    while True:
        print_menu()

        # I am letting user know that they must only enter one of the characters in paranthesis
        user_choice = get_char_from_user("What would you like to do? (L, A, E, D, or Q?): ", 'laedqLAEDQ')
        print()
        if ((user_choice == "l") or (user_choice == "L")):
            list_movies(movie_list)
        elif ((user_choice == "a") or (user_choice == "A")):
            add_movie(movie_list)
        elif ((user_choice == "e") or (user_choice == "E")):
            edit_movie(movie_list)
        elif ((user_choice == "d") or (user_choice == "D")):
            delete_movie(movie_list)
        elif ((user_choice == "q") or (user_choice == "Q")):
            print("Good bye!")
            break
        else:
            print("That is not a valid choice.")


main()
