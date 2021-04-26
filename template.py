# Taken from https://github.com/rajatg98/Competitive-Coding-Python-Template/blob/master/template.py

import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

ii = lambda: int(input())  # In input
si = lambda: input().strip()  # String input
jn = lambda x, l: x.join(map(str, l))
strl = lambda: list(input().strip())
mul = lambda: map(int, input().strip().split())
mulf = lambda: map(float, input().strip().split())
mulseq = lambda: list(map(int, input().strip().split()))

# Matrix operations
rotate_matrix = lambda matrix: list(zip(*matrix))[::-1]

# LL
def consll(a_list):
    curr = LLNode(a_list[0])
    head = curr

    for val in a_list[1:]:
        temp = LLNode(val)
        curr.next = temp
        curr = temp

    return head


stdinp = lambda x: stdin.open(f"{x}.in", "r")
stdopt = lambda x: stdin.open(f"{x}.out", "w")

# Not sure how useful these two are
ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1

stdinp = lambda x: stdin.open(f"{x}.in", "r")
stdopt = lambda x: stdin.open(f"{x}.out", "w")

# Or these
flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr = lambda x: stdout.write(str(x))


matrix = [[6, 9, 8], [1, 8, 0], [5, 1, 2], [8, 0, 3], [1, 6, 4], [8, 8, 10]]

print(rotate_matrix(matrix))
