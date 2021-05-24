import math
import statistics

num_ducks = int(input())

ducks = []
cols = []
rows = []

for i in range(num_ducks):
    col, row = map(int, input().split())
    cols.append(col)
    rows.append(row)
    ducks.append((col, row))

rows.sort()
cols.sort()

rh = statistics.median_high(rows)
rl = statistics.median_low(rows)
ch = statistics.median_high(cols)
cl = statistics.median_low(cols)

things = [rh, rl]
more_things = [ch, cl]

curr_min = float("inf")
for thing in things:
    curr = 0
    for duck in ducks:
        curr += abs(duck[1] - thing)
    curr_min = min(curr_min, curr)

for thing in more_things:
    curr = 0
    for duck in ducks:
        curr += abs(duck[0] - thing)
    curr_min = min(curr_min, curr)

print(curr_min)