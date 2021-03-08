# Classic knapsack problem


def knapsack(weights, values, max_weight):
    # 2d array of sides items/knapsack capacities
    dp = [[None for j in range(max_weight + 1)] for i in range(len(values) + 1)]

    num_items = len(weights)

    for i in range(num_items):
        weight = weights[i]
        value = values[i]

        for size in range(max_weight):
            # The row directly above
            dp[i][size] = dp[i - 1][size]

            # Not clear on this bit yet, checking diagonal

            # If the weight fits inside the subproblems knapsack
            # AND the row above (max value/remaining weight after including current item) plus current value is greater than current value (of the row directly above)..
            if size >= weight and dp[i - 1][size - weight] + value > dp[i][size]:
                # Set current index to the max val with remaining weight plus the value of the current item
                dp[i][size] = dp[i - 1][size - weight] + value

    # Still need to backtrack to grab the items

    # for row in dp:
    #     print(row)


knapsack([1, 5, 2, 4], [3, 2, 6, 4], 20)