"""
How many ways are there to traverse a 2x2 grid, if you can only go downwards or right?

Optimizations: 
1. All grids of a certain x/y value have same # of solutions, so we can 'cache' the solutions for x/y values (using a memo)
"""


def recursive_solution(
    x, y, solution_cache={}
):  # Only intiialize empty cache if top level call is made to function

    key = f"{x},{y}"
    if key in solution_cache:
        return solution_cache[key]

    if x == 1 and y == 1:  # If it is a 1x1 grid, there is only one way to traverse it.
        return 1
    elif x == 0 or y == 0:  # Can't have a side length less than 1
        return 0

    solution_cache[key] = recursive_solution(
        x - 1, y, solution_cache
    ) + recursive_solution(x, y - 1, solution_cache)

    return solution_cache[key]  # Sum of going downward + going rightwards


print(recursive_solution(100, 100))  # O(n) solution
