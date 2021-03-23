import random
# RPS Component 3 - Compare user choice and computer choice V3
rps_list = ["rock", "scissors", "paper"]
comp_index = random.randint(-2, 0)
for item in rps_list:
    user_index = random.randint(-2, 0)
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options
        if user_index == comp_index:
            result = "Tie"
        elif user_index == comp_index - 1 or +2:
            result = "Lose"
        elif user_index == comp_index + 1 or -2:
            result = "Win"
    print("You chose {} and COM chose {}".format(user_choice, comp_choice))
    print("You {}!".format(result))