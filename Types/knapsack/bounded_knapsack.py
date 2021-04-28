# Could solve by converting into standard knapsack, O(W*n*M) -> too slow
# https://codeforces.com/blog/entry/65202?#comment-492168 (dorijanlendvaj's comment)

from typing import List, Tuple
import math


def findNextLowestPow2(n):
    """
    Might be sketch, the first line is only change
    OG code was for finding next pow 2, but idk bitwise so yolo
    """
    n = n // 2 + 1  # This might screw up stuff
    count = 0

    if n and not (n & (n - 1)):
        return n

    while n != 0:
        n >>= 1
        count += 1

    return 1 << count


def conversion(n) -> List[int]:
    nums = []
    count = n

    while count > 0:
        val = findNextLowestPow2(count)

        # not sure if needed
        if val in nums:
            break

        count -= val
        nums.append(val)

        # Do I need a check to see if count - val is less than zero (if so it is issue)?

    return nums


def convert(weight, value, amount) -> None:
    weights = []
    values = []

    for num in conversion(amount):
        weights.append(weight * num)
        values.append(value * num)

    print(weights)
    print(values)


convert(1, 2, 20)
