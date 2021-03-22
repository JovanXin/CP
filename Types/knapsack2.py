w = [1, 2, 4, 2, 5]
v = [5, 3, 5, 3, 2]

TOTAL_WEIGHT = 10
stored = [[None] * len(w)] * TOTAL_WEIGHT
print(stored)


def knapsack(pointer_pos, total_weight):
    print(f"{pointer_pos=}, {total_weight=}")
    if stored[pointer_pos][total_weight]:
        return stored[pointer_pos][total_weight]
    elif pointer_pos == 0 or total_weight == 0:  # No items left to consider or weight
        result = 0
    elif w[pointer_pos] > total_weight:
        result = knapsack(pointer_pos - 1, total_weight)
    else:
        tmp1 = knapsack(pointer_pos - 1, total_weight)
        tmp2 = v[pointer_pos] + knapsack(pointer_pos - 1, total_weight - w[pointer_pos])
        result = max(tmp1, tmp2)

    stored[pointer_pos][total_weight] = result
    return result


x = knapsack(len(w) - 1, TOTAL_WEIGHT)
print(x)
