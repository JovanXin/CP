import math

num = int(input())
nums = list(map(int, input().split()))

sum_num = (num * (num + 1)) / 2


print(int(abs(sum(nums) - sum_num)))