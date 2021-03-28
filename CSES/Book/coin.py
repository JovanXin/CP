"""
Given a list of coin values and a target number, return the minimum amount of coins required 
to reach that target.

Recursive solution using memoization to save the min coins required for each amount

TODO -> Figure out time complexity of this solution
"""

coins = (1, 3, 4)
memoization = {}


def coin(target):
    if target < 0:
        return float("inf")
    elif target in memoization.keys():
        return memoization[target]
    elif target == 0:
        return 0

    best = float("inf")
    for c in coins:
        # +1 cause we have to count the current coin that's been subtracted
        best = min(best, coin(target - c) + 1)
        memoization[target] = best

    return best


print(coin(int(input())))