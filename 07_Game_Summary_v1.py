game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 5

for item in range (0, 5):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "tie":
        rounds_drawn += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_drawn - rounds_lost

# calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print()
print("Win: {}, ({:.0f}%)\nLoss: ")