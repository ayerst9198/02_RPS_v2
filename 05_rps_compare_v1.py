# Rps Component 1 ~ generate computer choice

import random


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an iten), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()

# Main routine goes here
error = "You broke the game"

# lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / "
                                 "scissors (r/p/s) ", rps_list,
                                 "Please choose from rock / "
                                 "paper / scissors "
                                 "(or xxx to quit)")

    comp_choice = random.choice(rps_list[:-1])

    if comp_choice != user_choice:
        if comp_choice == "rock" and user_choice == "paper":
            print()
            print("You chose {} and COM chose {}".format(user_choice, comp_choice))
            print()
            print("You Win!")
            print()
        elif comp_choice == "paper" and user_choice == "scissors":
            print()
            print("You chose {} and COM chose {}".format(user_choice, comp_choice))
            print()
            print("You Win!")
            print()
        elif comp_choice == "scissors" and user_choice == "rock":
            print()
            print("You chose {} and COM chose {}".format(user_choice, comp_choice))
            print()
            print("You Win!")
            print()
        elif comp_choice == "paper" and user_choice == "rock":
            print()
            print("You chose {} and COM chose {}".format(user_choice, comp_choice))
            print()
            print("You Lose!")
            print()
        elif comp_choice == "scissors" and user_choice == "paper":
            print()
            print("You chose {} and COM chose {}".format(user_choice, comp_choice))
            print()
            print("You Lose!")
            print()
        elif comp_choice == "rock" and user_choice == "scissors":
            print()
            print("You chose {} and COM chose {}".format(user_choice, comp_choice))
            print()
            print("You Lose!")
            print()
    elif comp_choice == user_choice:
        print()
        print("You chose {} and the Com chose {}".format(user_choice, comp_choice))
        print()
        print("Tie!")
        print()
    else:
        print()
        print(error)
        print()