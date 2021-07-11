"""
100/100
Issues Faced
1) Accidentally screwed up comparisons between efficency of 2 duck vs 3 duck
    -> Confused myself with the name "efficency" wheras it really should be "cost
2) Distracted myself with recursive attempt 
    -> Should've realized a greedy solution was fine    

Overall, code was very messy since I rushed into it. 
"""
ducks_to_buy = int(input())
two_ducks_cost = int(input())
three_ducks_cost = int(input())

curr_cost = 0

three_ducks_efficency = three_ducks_cost/3
two_ducks_efficency = two_ducks_cost/2

if three_ducks_efficency < two_ducks_efficency:
    remainder = ducks_to_buy % 3
    amount = (ducks_to_buy - remainder) // 3
    curr_cost += amount * three_ducks_cost

    if remainder == 1:
        curr_cost -= 1 * three_ducks_cost
        curr_cost += 2 * two_ducks_cost
    elif remainder == 2:
        curr_cost += two_ducks_cost
    print(curr_cost)
elif two_ducks_efficency < three_ducks_efficency:
    able = ducks_to_buy % 2
    amount = (ducks_to_buy - able) // 2

    curr_cost += amount * two_ducks_cost

    if able == 1:
        curr_cost -= 1 * two_ducks_cost
        curr_cost += 1 * three_ducks_cost
    
    print(curr_cost)


elif two_ducks_efficency == three_ducks_efficency:
    curr_cost_1 = 0
    able = ducks_to_buy % 2
    amount = (ducks_to_buy - able) // 2
    curr_cost += amount * two_ducks_cost

    if able == 1:
        curr_cost -= 1 * two_ducks_cost
        curr_cost += 1 * three_ducks_cost
    
    able = ducks_to_buy % 3
    amount = (ducks_to_buy - able) // 3
    curr_cost_1 += amount * three_ducks_cost

    if able == 1:
        curr_cost_1 -= 1 * three_ducks_cost
        curr_cost_1 += 2 * two_ducks_cost
    elif able == 2:
        curr_cost_1 += 1 * two_ducks_cost

    print(min(curr_cost, curr_cost_1))