# CS223 HW4 - Contact List with Classes - Instructor Dan Eshner
# By Tiffany Hodges on 11/17/2020
# A mix of sources were used to aid me in my code. Each source has been commented
# next to where it was used
# Peer reviews by:
# This is a program that holds a list of contacts with several attributes like name, age, gender, etc.
# The list can be manipulated (adding, editing, and deleting a contact)
# User can also choose to list all contacts to see what is in the list
# When user exits the program, the list will go back to its original form (3 listings)
# This is a beginner's program as this is my first python class, therefore
# the code itself is far from advanced


# used for regular expressions to check the email and phone number
import re

# here are all the constants used throughout my code
GENDER_CHARS = 'mfoMFO'
DECISION_CHARS = 'ynYN'
MENU_CHARS = 'ladeqLADEQ'
BEGIN_AGE = 1
END_AGE = 110

#-------------START CHECKS---------------
#These are all functions that check for valid user input

# function to get valid gender character
# will first check that only one char is entered
# then checks that user input is one of these char: mMfFoO
def check_gender(prompt, GENDER_CHARS):
    while True:
        user_input = input(prompt)
        if len(user_input) != 1:
            print("Please enter only a single letter")
        elif user_input not in GENDER_CHARS:
            print("That character is not valid, please try again.")
        else:
            return user_input

# function similar to above but to check for valid yes or no (ynYN)
def get_choice_from_user(prompt, DECISION_CHARS):
    while True:
        user_input = input(prompt)
        if len(user_input) != 1:
            print("Please enter only a single letter")
        elif user_input not in DECISION_CHARS:
            print("That character is not valid, please try again.")
        else:
            return user_input

# function to check for a string that is only letters
# will first check to be sure user actually enters something rather than empty string
# this function will also allow spaces since city names have spaces (Palm Springs) along with
# names (Mary Jo). Received help from this thread:
# https://stackoverflow.com/questions/20890618/isalpha-python-function-wont-consider-spaces
def check_for_chars(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) <= 0:
            print("Must be at least 1 character. Try again.")
        elif not all(x.isalpha() or x.isspace() for x in user_input):
            print("Must only contain letters.")
        else:
            return user_input

# function to check for valid char for the menu options, and that only 1 char is entered
def get_menu_option_from_user(prompt, MENU_CHARS):
    while True:
        user_input = input(prompt)
        if len(user_input) != 1:
            print("Please enter only a single letter")
        elif not user_input in MENU_CHARS:
            print("That character is not valid, please try again.")
        else:
            return user_input

# function to check for a valid phone number in a specific format
# will also check that user is not entering empty string and checks for letters which are not allowed
def check_phone(prompt):
    while True:
        user_input = input(prompt)

        #citing source: https://automatetheboringstuff.com/chapter7/
        #First, I create a regex object (valid_phone), then transform the string into raw string (r)
        #I specifically want user to use this format: XXX-XXX-XXXX (\d\d\d-\d\d\d-\d\d\d\d) to keep it consistent, nice and clean
        #Then, I pass the string I'm looking for into regex object’s search() method
        valid_phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        if (re.search(valid_phone, user_input)): #searching for the specific formatted string
            return user_input  
        elif user_input.isalpha(): #making sure input is NOT letters
            print("Cannot contain letters.")
        elif len(user_input) <= 0:
            print("Cannot be blank, try again.")  
        else:
            print("Invalid format, try again.")
        
def check_email(prompt):
    while True:
        user_input = input(prompt)

        # taking the same concept from check_phone(), found this website for regex to check for
        # valid email: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        # I did it this way because I want user to use specific format: xxxxx@xxxx.com so that emails
        # are consistent, neat & clean within the list
        valid_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        if (re.search(valid_email, user_input)): #searching for the specific formatted string
            return user_input
        elif len(user_input) <= 0:
            print("Cannot be blank, try again.")  
        else:  
            print("Invalid format, try again.")


# function to check user input for a numeric age within range 1-110
# of course checks to make sure user actually inputs something rather than empty string
def check_age(prompt, BEGIN_AGE, END_AGE):
    while True:
        user_input = input(prompt)
        if not user_input.isdecimal():
            print("You have entered an invalid character. Please only enter a number.")
            print()
        elif len(user_input) <= 0:
            print("Must not be blank. Try again.")
            print()
        else:
            user_int = int(user_input)
            if user_int < BEGIN_AGE or user_int > END_AGE:
                print("The age entered is invalid. Must be between 1-110.")
                print()
            else:
                return user_int

# function to check for digits, used within the add and edit_contact() functions
# purpose of this function is mainly to make sure user is only entering a number as opposed to letters or other special chars
def check_for_int(prompt, begin_range=0, end_range=1000):
    while True:
        user_input = input(prompt)
        if not user_input.isdecimal():
            print("You have entered an invalid character. Please only enter a number.")
            print()
        else:
            user_int = int(user_input)
            if user_int < begin_range or user_int > end_range:
                print("The number entered is out of range. Please try again.")
                print()
            else:
                return user_int

#----------------END CHECKS-------------------------------------

# class that handles everything having to do with a single instance of a contact
class contact:
    def __init__(self, p_fname, p_lname, p_gender, p_age, p_city, p_phone, p_email): #instance creation
        self.MAX_AGE = END_AGE
        self.fname = p_fname
        self.lname = p_lname
        self.gender = p_gender
        self.age = p_age
        self.city = p_city
        self.phone = p_phone
        self.email = p_email


    # to print a single contact
    def print_contact(self):
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname} ")
        print(f"Gender: {self.gender} ")
        print(f"Age: {self.age}")
        print(f"Current City: {self.city} ")
        print(f"Phone #: {self.phone} ")
        print(f"Email: {self.email} ")

    # getters and setters for each attribute in the contact class
    @property 
    def first_name(self):
        return self.fname

    @first_name.setter
    def first_name(self, new_fname):
        if len(new_fname) > 0:
            self.fname = new_fname

    @property 
    def last_name(self):
        return self.lname

    @last_name.setter
    def last_name(self, new_lname):
        if len(new_lname) > 0:
            self.lname = new_lname

    @property
    def the_gender(self):
        return self.gender

    @the_gender.setter
    def the_gender(self, new_gender):
        if len(new_gender) == 1:
            self.gender = new_gender

    @property 
    def the_age(self):
        return self.age

    @the_age.setter
    def the_age(self, new_age):
        if 1 <= new_age <= self.MAX_AGE:
            self.age = new_age

    @property
    def the_city(self):
        return self.city
    
    @the_city.setter
    def the_city(self, new_city):
        if len(new_city) > 1:
            self.city = new_city

    @property
    def the_phone(self):
        return self.phone
    
    @the_phone.setter
    def the_phone(self, new_phone):
        if len(new_phone) == 12:
            self.phone = new_phone

    @property
    def the_email(self):
        return self.email

    @the_email.setter
    def the_email(self,new_email):
        if len(new_email) > 4:
            self.email = new_email

# class that handles everything having to do with the list of contacts (adding, deleting, editing, listing all contacts)
class contact_list:
    def __init__(self):
        # I hard-coded a few contacts into the list so user can start with some data already in the list
        self.contact_list = [["Jim", "Carrey", "M", 58, "Los Angeles", "213-968-0252", "jimcarrey@gmail.com"],
                        ["Ewan", "McGregor", "M", 49, "London", "213-495-7762", "emcgregor@hotmail.com"],
                        ["Emma", "Watson", "F", 30, "New York", "718-778-2324", "watsonem@comcast.net"]]
    
    # Function that will print all contacts and their attributes in the list
    # if list is empty, user will be told then taken back to main menu
    # since I am using a 2D array, the indexes are as follows: 0 for first name, 1 for last name, 2 for gender, 3 for age, etc.
    def print_all_contacts(self):
        if len(self.contact_list) > 0:
            for contact in range(0, len(self.contact_list)):
                print("Contact #", contact, "| Name:", self.contact_list[contact][0], self.contact_list[contact][1],
                "| Gender:", self.contact_list[contact][2], "| Age:", self.contact_list[contact][3], "| City:",
                self.contact_list[contact][4], "| Phone:", self.contact_list[contact][5], "| Email:", self.contact_list[contact][6])
        else:
            print("There are no contacts to display. Try adding some contacts.")

    # function to gather all info of a new contact from user
    # all variables will be checked for proper input
    # once user has provided all info, a variable new_contact will be used to hold all the new data
    def get_contact_info(self):
        first_name = check_for_chars("Please enter the first name: ")
        last_name = check_for_chars("Please enter the last name: ")
        gender = check_gender("Enter a gender (M, F, O): ", GENDER_CHARS)
        age = check_age("Enter an age: ", BEGIN_AGE, END_AGE)
        city = check_for_chars("Please enter their current city: ")
        phone = check_phone("Enter their phone number (XXX-XXX-XXXX): ")
        email = check_email("Enter their email with @ and .com/.net, etc. (xxxx@xxxx.xxx): ")
        print()
        new_contact = contact(first_name, last_name, gender, age, city, phone, email)
        return new_contact

    # this function passes all the info from the get_contact_info into new variable contact_to_add
    # I did this in order to get the data into an iterable format for the list.
    # this allows the print statement to function. (Otherwise, error when trying to iterate a contact object)
    # Since I am using a 2d array, index 0 is the first name. When appending to the list, index position of
    # appended item will always be -1, hence I am able to tell user the name of the contact they added by
    # locating it's position within the list [-1], then the first attribute which is first name [0]
    def add_contact(self):
        new_contact = self.get_contact_info()
        contact_to_add = [new_contact.first_name, new_contact.last_name, new_contact.gender, new_contact.age,
                        new_contact.city, new_contact.phone, new_contact.email]
        self.contact_list.append(contact_to_add)
        print("You have added '", self.contact_list[-1][0] + " " + self.contact_list[-1][1], "' to your Contacts List.")

    # function to remove/delete a contact from the list
    # will first make sure there are contacts in the list, then will print the contact menu with their corresponding index #'s
    # user will enter the index # of contact they want to delete, if # doesn't exist they will be told to try again
    # once they have entered a valid index #, they will be asked to confirm the deletion of the contact
    def delete_contact(self):
        while True: 
            if len(self.contact_list) > 0:
                self.print_all_contacts()
                print()
                contact_to_delete = check_for_int("Enter the contact # you would like to delete: ", 0, 1000)
                if contact_to_delete in range(0, len(self.contact_list)):
                    delete_decision = get_choice_from_user("Are you sure you want to delete " + 
                                      str(self.contact_list[contact_to_delete][0]) + " " +
                                      str(self.contact_list[contact_to_delete][1]) + "? (y/n): ", DECISION_CHARS)
                    print()
                    if ((delete_decision == "y") or (delete_decision == "Y")):
                        print(str(self.contact_list[contact_to_delete][0]) + " " +
                        str(self.contact_list[contact_to_delete][1]) + " has been deleted.")
                        del self.contact_list[contact_to_delete]
                        break
                    else:
                        print(".....Exiting delete mode.....")
                        break
                else:
                    print("That contact # does not exist.")
                    print()
            else:
                print("There is nothing to delete because the Contacts List is empty.")
                break

    # function to edit a contact, very similar to the delete function
    # it will check to make sure the contact list is not empty, then print the list of contacts
    # user will be asked to enter the # of contact they want to edit, then confirm if that is the one they want to edit
    # if user decide they do not want to edit, it will kick back to main menu
    # otherwise, if user decides yes then they will be asked to enter all new input for each attribute of the contact object
    def edit_contact(self):
        while True:
            if len(self.contact_list) > 0:
                self.print_all_contacts()
                print()
                contact_to_edit = check_for_int("Please enter the contact # you would like to edit: ", 0, 1000)
                if contact_to_edit in range(0, len(self.contact_list)):
                    edit_decision = get_choice_from_user("You are about to edit contact " + str(self.contact_list[contact_to_edit][0]) + 
                                    " " + str(self.contact_list[contact_to_edit][1]) + ". Are you sure? (y/n): ", 'ynYN')
                    print()
                    if ((edit_decision == "y") or (edit_decision == "Y")): 
                        edited_fname = check_for_chars("Enter the new First Name: ")
                        self.contact_list[contact_to_edit][0] = edited_fname

                        edited_lname = check_for_chars("Enter the new Last Name: ")
                        self.contact_list[contact_to_edit][1] = edited_lname

                        edited_gender = check_gender("Enter the new gender (M, F, or O): ", GENDER_CHARS)
                        self.contact_list[contact_to_edit][2] = edited_gender

                        edited_age = check_age("Enter the new Age: ", BEGIN_AGE, END_AGE)
                        self.contact_list[contact_to_edit][3] = edited_age

                        edited_city = check_for_chars("Enter the new City: ")
                        self.contact_list[contact_to_edit][4] = edited_city

                        edited_phone = check_phone("Enter the new Phone # (XXX-XXX-XXXX): ")
                        self.contact_list[contact_to_edit][5] = edited_phone

                        edited_email = check_email("Enter the new email with @ and .com/.net etc. (xxxx@xxxxx.com): ")
                        self.contact_list[contact_to_edit][6] = edited_email

                        new_contact = [edited_fname, edited_lname, edited_gender, edited_age, edited_city, edited_phone, edited_email]
                        self.contact_list[contact_to_edit] = new_contact
                        print("\n.....Edit successful.....")
                        print()
                        break
                    else:
                        print("\n.....Exiting edit mode.....")
                        break
                else:
                    print("That contact # does not exist. Please try again.")
                    print()
            else:
                print("There is nothing to edit because the Contact List is empty.")
                break
   
    # prints the welcome page with menu options
    def print_menu():
        print(
            """
            Welcome to your Contacts List

            (L)ist – List all contacts
            (A)dd – Add a new contact
            (E)dit – Edit an existing contact
            (D)elete – Delete a contact
            (Q)uit – Exit the program
        
            """
            )

# function to run the main program
# passes the contact_list() into contacts
# prints welcome page with menu options, asks user for their choice
def main(contact_list):
    user_choice = None
    contacts = contact_list()

    # main logic loop to get user's choice which will call the corresponding function
    # user must select a valid option or else they will be asked to try again
    # loop will always print the welcome statement with their choices after they have completed each selection all the way through
    # if user decides to quit, the program will stop running and contact list will go back to its original form (3 listings)
    while True:
        contact_list.print_menu()

        # I am letting user know that they must only enter one of the characters in paranthesis
        user_choice = get_menu_option_from_user("What would you like to do? (L, A, E, D, or Q?): ", MENU_CHARS)
        print()
        if ((user_choice == "l") or (user_choice == "L")):
            contacts.print_all_contacts()
        elif ((user_choice == "a") or (user_choice == "A")):
            contacts.add_contact()
        elif ((user_choice == "e") or (user_choice == "E")):
            contacts.edit_contact()
        elif ((user_choice == "d") or (user_choice == "D")):
            contacts.delete_contact()
        elif ((user_choice == "q") or (user_choice == "Q")):
            print("Good bye!")
            break
        else:
            print("That is not a valid choice.")

main(contact_list)
