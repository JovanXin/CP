from typing import List


def knapsack(weights: List[int], values: List[int], max_weight: int):
    dp = [[0] * (max_weight + 1) for _ in range(len(values) + 1)]

    # Implementation of tabulation
    for i in range(1, len(values) + 1):
        value = values[i - 1]
        weight = weights[i - 1]

        for j in range(1, max_weight + 1):
            dp[i][j] = dp[i - 1][j]

            # If the item weighs less than the capacity avaliable
            if j >= weight:
                # Current dp value is max(row above not including curr item, row above - weight to find optimum without current item weight plus extra value current item gives)
                dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i][j])

    # Backtrack through to find the knapsack items used
    y, x = len(values), max_weight

    used_values = []
    # While not at origin
    while dp[y][x] != dp[0][0]:
        # If we have taken current item (since it is not same as item in row above)
        if dp[y][x] > dp[y - 1][x]:
            used_values.append(y)
            y -= 1
            x -= weights[y]
        else:
            y -= 1

    return used_values


# Testing
weights = [3, 1, 3, 4, 2]
values = [2, 2, 4, 5, 3]

used_vals = knapsack(weights, values, 7)
print(used_vals)  # Items 5, 4 and 2 should be optimally used
