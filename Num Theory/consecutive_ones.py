def solve(nums):
    start = nums.index(1)
    end = nums.rindex(1)  # Why doesn't this work?
    print(start)
    print(end)


print(solve([0, 1, 0, 3, 7, 1, 6, 3, 2]))