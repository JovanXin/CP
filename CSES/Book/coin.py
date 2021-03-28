"""
Given a list of coin values and a target number, return the minimum amount of coins required 
to reach that target.

Extra -> Return # of possible ways to reach the target num.
"""

coins = (1, 3, 4)
SUM = 10

# Best is getting redefined as infinity every time? something about scope?? idfk


def work(sum):
    if sum == SUM:
        best = float("inf")
    if sum == 0:
        return 0

    for c in coins:
        best = max(best, (work(sum - c) + 1))
        return best


x = work(SUM)
print(x)