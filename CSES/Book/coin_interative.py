"""
Same as the previous coin problem, except this time solved recursively

Added the coins needed to reach that amount -> kinda broken
"""

coins = (1, 3, 4)


def coin(target):
    required_coins = []
    values = [0]
    for i in range(1, target + 1):
        values.append(float("inf"))

        for c in coins:
            if i - c >= 0 and values[i - c] + 1 < values[i]:
                values[i] = values[i - c] + 1
                required_coins.append(c)

    n = len(required_coins)
    while n > 0:
        print(required_coins[n - 1], end=", ")
        n -= required_coins[n - 1]

    return values[target]  # Return index at 4


print(coin(int(input())))