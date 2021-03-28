"""
Given a list of coin values and a target number, return the minimum amount of coins required 
to reach that target.

Current solution is probably O(2^n?) cause of the extra branches repeated...
Extra -> Return # of possible ways to reach the target num.
"""

# Best is getting redefined as infinity every time? something about scope?? idfk

import math

coins = (1, 3, 4)


def coin(target):
    if target < 0:
        return float("inf")
    elif target == 0:
        return 0

    best = float("inf")
    for c in coins:
        best = min(
            best, coin(target - c) + 1
        )  # +1 cause we have to count the current coin that's been subtracted

    return best


print(coin(int(input())))