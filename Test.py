import random

individual_genetis = ["the idea is great"]

# Randomly select a stopping point
stopping_point = random.randint(1, len(individual_genetis[0]) - 1)

# Divide the list into two parts
part1 = individual_genetis[0][:stopping_point]
part2 = individual_genetis[0][stopping_point:]

if __name__ == "__main__":
    print(len(individual_genetis[0]))
    print("Part 1:", part1)
    print("Part 2:", part2)