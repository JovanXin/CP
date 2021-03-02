

class Solution:
    def solve(self, nums):
        nums_count = nums.count(1)

        location = nums.index(1)
        second = nums.rindex(1) # Why doesn't this work?
        print(location)
