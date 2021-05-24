"""
My crucial error was that I used mean instead of the medians to try calculate my final answer...
"""

import math

ducks = []
t_c, t_r = 0, 0
duck_n = int(input())


for i in range(duck_n):
    c, r = map(int, input().split())
    ducks.append((c, r))
    t_c += c
    t_r += r

avg_c_ceil = math.ceil(t_c / duck_n)
avg_c_floor = math.floor(t_c / duck_n)
# finding avg column
avg_r_ceil = math.ceil(t_r / duck_n)
avg_r_floor = math.floor(t_r / duck_n)

c_dist_ceil, c_dist_floor, r_dist_ceil, r_dist_floor = 0, 0, 0, 0
for duck in ducks:
    c_dist_ceil += abs(duck[0] - avg_c_ceil)
    c_dist_floor += abs(duck[0] - avg_c_floor)
    r_dist_ceil += abs(duck[1] - avg_r_ceil)
    r_dist_floor += abs(duck[1] - avg_r_floor)

print(min(c_dist_floor, c_dist_ceil, r_dist_floor, r_dist_ceil))

# d1_c, d1_r = map(int, input().split())
# d2_c, d2_r = map(int, input().split())

# if abs(d1_c - d2_c) < abs(d1_r - d2_r):
#     c = (d1_c + d2_c) // 2
#     dist = abs(d1_c - c) + abs(d2_c - c)
# else:
#     r = (d1_r + d2_r) // 2
#     dist = abs(d1_r - r) + abs(d2_r - r)

# print(dist)