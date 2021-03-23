import random

# Functions go here


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Plese input yes / no")


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


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here


rounds_lost = 0
rounds_drawn = 0
rounds_played = 0

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

# Asks user if they have played before.

# If 'no' show instructions


# ask user for # of rounds then loop
end_game = "no"
while end_game == "no":

    # Rounds heading
    #Check if Continuous

    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played)


    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        # End game if exit code is typed
        if rounds_played == "":
            end_game = "yes"

    print(heading)

    choose_instruction = "Please choose rock (r), paper " \
                        "(p), or scissors (s): "

    choose_error = "Please choose from rock / " \
                    "paper / scissors (or xxx to quit)"

    # Ask user for choice and check it's valid

    choose = choice_checker(choose_instruction, rps_list,
                            choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # compare choices
    if choose == "rock":
        if comp_choice == "paper":
            result = "lose"
            rounds_lost += 1
        if comp_choice == "scissors":
            result = "win"

    if choose == "paper":
        if comp_choice == "scissors":
            result = "lose"
            rounds_lost += 1
        if comp_choice == "rock":
            result = "win"

    if choose == "scissors":
        if comp_choice == "paper":
            result = "win"
        if comp_choice == "rock":
            result = "lose"
            rounds_lost += 1

    if choose == comp_choice:
        result = "tied"
        rounds_drawn += 1

    #  End game if exit code is typed

    if choose == "xxx":
        print()
        break

    if result == "tied":
        feedback = "It's a tie "
    else:
        feedback = "You chose {} and com chose {} - you {}".format(choose, comp_choice, result)


    # rest of loop / game

    print(feedback)
    print()

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Display Game Summary

rounds_won = rounds_played - rounds_lost - rounds_drawn
print("***** History *****")
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thank you for playing")

# Ask user if they want to see their game history
History = yes_no("Do you want to see your history? ")
# If 'yes' show history
if History == "yes":
    rounds_won = rounds_played - rounds_lost - rounds_drawn
    print()
elif History == "no":
    print()