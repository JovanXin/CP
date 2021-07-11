"""
57/100
Issues faced
1) Initially, was storing all competitiors in dictionary. Too memory intensive.
2) Linear search through the changed list was too slow -> fixed with bisect module
3) Memory Limit Exceeded -> unsolved
    Post-contest: 
        1) Changed when we create competitors in the dictionary, only store state if operation is to change.
           Otherwise, if we want to output only create state if player is not already in dictionary
            -> Not sure if this actually helps though 
        2) Reduce number of comparisons? When outputting if num not in competitors we just print num - i
           instead of creating the competitor in dictionary first 

TODO
[] Check if optimizations are enough to get > 57
"""

import bisect

num_competitors = int(input())
competitors = {}
num_queries = int(input())

changed = []
for query in range(num_queries):
    char, num = input().split()
    num = int(num)

    if char == "t":
        if num not in competitors:
            competitors[num] = False
            bisect.insort(changed, num)
        elif num in competitors:
            if competitors[num] == True:
                competitors[num] = False
            elif competitors[num] == False:
                competitors[num] = True
            if num in changed:
                changed.remove(num)
            else:
                bisect.insort(changed, num)
    elif char == "o":
        i = bisect.bisect_left(changed, num)
        if num not in competitors:
            print(num - i)
        elif competitors[num] == True:
            print(num - i)
        else:
            print("UNOFFICIAL")
