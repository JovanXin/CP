"""
Same as the previous coin problem, except this time solved recursively
"""

coins = (1, 3, 4)


def coin(target):
    values = [0]
    for i in range(1, target):
        values.append(float("inf"))

        for c in coins:
            if i - c >= 0:
                values[i] = min(values[i], values[i - c] + 1)

    return values[target - 1]  # Return index at 4


print(coin(int(input())))