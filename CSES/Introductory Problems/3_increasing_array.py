arr_size = int(input())
nums = map(int, input().split())

curr_max = 0
min = 0

for num in nums:
    print(num)
    mx = max(num, curr_max)
    min += mx - num

print(min)