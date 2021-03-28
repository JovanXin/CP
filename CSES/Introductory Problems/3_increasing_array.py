arr_size = int(input())
nums = list(map(int, input().split()))

needed = 0

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        needed += nums[i] - nums[i + 1]
        nums[i + 1] = nums[i]


print(needed)
