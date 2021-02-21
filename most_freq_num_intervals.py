# My very inefficent bruteforce solution...


class Solution:
    def solve(self, intervals):
        nums = {}
        most_freq_num = 0
        current_freq = 0

        for interval in intervals:
            for num in range(interval[0], interval[1] + 1):
                if num in nums.keys():
                    nums[num] += 1
                else:
                    nums[num] = 1

        for num, freq in nums.items():
            if freq > current_freq:
                most_freq_num = num
                current_freq = freq
            elif freq == current_freq and num < most_freq_num:
                most_freq_num = num

        return most_freq_num


# A more efficent solution?
class Solution:
    def solve(self, intervals):
        nums = [0 for i in range(100001)]

        for interval in intervals:
            for i in range(interval[0], interval[1] + 1):
                nums[i + 1] += 1

        return nums.index(max(nums)) - 1
