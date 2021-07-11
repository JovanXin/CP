"""
Issues faced
1) Max recursion depth error -> Solved with setting the recursion limit
2) Messed up recursion -> couldn't figure out how to return 'cost' for a bit
3) Memoization was screwed up, needed both num ducks and current cost, not just ducks 
4) Final issue that was unsolved... TLE
All this brang me back to the original greedy implemenation
"""

import sys
sys.setrecursionlimit(10**6)

ducks_to_buy = int(input())
two_ducks_cost = int(input())
three_ducks_cost = int(input())

ducks = {
    two_ducks_cost: 2,
    three_ducks_cost: 3,
}


memoize = {}

def recursively_solve(num_ducks, current_cost):
    if (num_ducks, current_cost) in memoize:
        return memoize[(num_ducks, current_cost)]
    if num_ducks < 0:
        return float("inf")
    elif num_ducks == 0:
        return current_cost
    cost = float("inf")

    for duck_cost, duck_amount in ducks.items():
        # print(f"{duck_amount=}, {duck_cost=}")
        cost = min(cost, recursively_solve(num_ducks - duck_amount, current_cost + duck_cost))

    memoize[(num_ducks, current_cost)] = cost
    return cost

print(recursively_solve(ducks_to_buy, 0))