"""
20/100
I think this was closer to my original attempt
"""
import bisect

num_competitors = int(input())
competitors = [[i, True] for i in range(1, num_competitors + 1)]
num_queries = int(input())

changed = []
for query in range(num_queries):
    char, num = input().split()
    num = int(num)

    if char == "t":
        if competitors[num - 1][1] == True:
            competitors[num - 1][1] = False
        elif competitors[num - 1][1] == False:
            competitors[num - 1][1] = True
        if num in changed:
            changed.remove(num) 
        else:
            bisect.insort(changed, num)
    elif char == "o":
        i = bisect.bisect_left(changed, num)
        if competitors[num - 1][1] == True:
            print(competitors[num - 1][0] - i)
        else:
            print("UNOFFICIAL")

