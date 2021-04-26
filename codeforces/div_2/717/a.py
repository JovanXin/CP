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

testcases = ii()

for t in range(testcases):
    n_el, max_operations = mul()
    arr = mulseq()
    nw_arr = arr

    for i in range(n_el):
        while arr[i] > 0 and max_operations > 0:
            max_operations -= 1
            arr[i] -= 1
            arr[n_el - 1] += 1

    print(*arr)