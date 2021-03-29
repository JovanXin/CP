"""
Same problem as before, but this time we count total number of solutions
for a value of 'x'

No clue if current solution is valid
"""

coins = (1, 3, 4)


def coin(target):
    solutions = [1]

    for i in range(1, target + 1):
        solutions.append(0)
        for c in coins:
            if i - c >= 0:  # if the index is positive
                solutions[i] += solutions[i - c]

    return solutions[target]


print(coin(int(input())))