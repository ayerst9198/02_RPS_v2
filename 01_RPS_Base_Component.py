import random
# functions go here


# makes statements look good P.S. I MADE THIS CODE
def statement_generator(statement, left_side_decoration, top_decoration, bottom_decoration, right_side_decoration):

    left_sides = left_side_decoration * 3

    right_sides = right_side_decoration * 3

    statement = "{} {} {}".format(left_sides, statement, right_sides)

    top_bottom = top_decoration * len(statement)

    bottom_bottom = bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(bottom_bottom)

    return ""


#  simplifies instructions
def instructions():
    statement_generator("How to play", "*", "?", "?", "*")
    print()
    print("Choose either a number of rounds or press <enter> for")
    print("  infinite mode, or i for infinite impossible mode")
    print()
    print("Then for each round, choose from rock")
    print("/ paper / scissors (or xxx to quit)")
    print("You can type r / p / s / x if you")
    print("don't want to type the entire word")
    print()
    print("The rules are...")
    print("- Rock beats scissors")
    print("- Scissors beats paper")
    print("- Paper beats rock")
    print()
    statement_generator("Have fun", "^", "*", "-", "*")
    return ""


# confines answers to yes / no
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
            print("Please input yes / no")


# checks rock, paper, or scissors
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


# checks rounds or infinite
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                if response == "i":
                    return response
                else:
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
result = "quitter"

# Lists of valid responses

yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
game_summary = []

# welcome user
statement_generator("Welcome to Rock Paper Scissors", "|", "^", "-", "|")
print()

# Asks user if they have played before.
show_instructions = yes_no("Have you played my "
                           "game before? ")

# If 'no' show instructions
if show_instructions == "no":
    print()
    instructions()
print()

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()


# ask user for # of rounds then loop
end_game = "no"
while end_game == "no":

    # Rounds heading

    # Check if Continuous or impossible

    print()
    if rounds == "":
        heading = statement_generator("Continuous Mode: Round {}".format(rounds_played + 1), "!", "!", "!", "!")

    elif rounds == "i":
        heading = statement_generator("Impossible Mode: Round {}".format(rounds_played + 1), "????", "", "", "????")


    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        # End game if exit code is typed
        if rounds_played == "":
            end_game = "yes"
            statement_generator(heading, "*", "*", "*", "*")


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
    if rounds == "i":
        if choose == "rock":
            comp_choice = "paper"
            result = "lose"
            rounds_lost += 1
        if choose == "paper":
            comp_choice = "scissors"
            result = "lose"
            rounds_lost += 1

        if choose == "scissors":
            comp_choice = "paper"
            result = "lose"
            rounds_lost += 1

    else:
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

    # add result to list
    game_summary.append(result)

    #  End game if exit code is typed

    if choose == "xxx":
        print()
        break

    if result == "tied":
        feedback = "???????? It's a tie ????????"
    elif result == "lose":
        feedback = "You chose {} and com chose {} - ??? you {} ???".format(choose, comp_choice, result)
    else:
        feedback = "You chose {} and com chose {} - ???????????? you {} ????????????".format(choose, comp_choice, result)


    # rest of loop / game

    print(feedback)
    print()

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Display Game Summary

rounds_won = rounds_played - rounds_lost - rounds_drawn
print("***** Summary *****")
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thank you for playing")

# Ask user if they want to see their game history
history = yes_no("Do you want to see your history? ")
# If 'yes' show history
if history == "yes":
    if result == "quitter":
        print()
        statement_generator("lol, you are a quitting loser", "????", "", "", "????")

    else:
        rounds_won = rounds_played - rounds_drawn - rounds_lost

        # calculate game stats
        percent_win = rounds_won / rounds_played * 100
        percent_lose = rounds_lost / rounds_played * 100
        percent_tie = rounds_drawn / rounds_played * 100

        print()
        statement_generator("***** Game History *****", "|", "*", "-", "|")
        for game in game_summary:
            print(game)

        print()

        # displays game stats with % values to the nearest whole number
        statement_generator("Game Statistics", "*", "?", "-", "*")
        print("Win: {}, ({:.0f}%)\nLoss: {}, "
              "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,
                                                     percent_lose, rounds_drawn, percent_tie))
        print("Thank you for playing")
else:
    print("Thank you for playing")