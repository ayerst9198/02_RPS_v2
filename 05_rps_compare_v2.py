# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options
        if user_choice == "rock":
            if comp_choice == "paper":
                result = "lose"
            if comp_choice == "scissors":
                result = "win"

        if user_choice == "paper":
            if comp_choice == "scissors":
                result = "lose"
            if comp_choice == "rock":
                result = "win"

        if user_choice == "scissors":
            if comp_choice == "rock":
                result = "lose"
            if comp_choice == "paper":
                result == "win"

        if user_choice == comp_choice:
            result = "tied"

        print("You chose {} and COM chose {}".format(user_choice, comp_choice))
        print("You {}!".format(result))
    comp_index += 1
    print()