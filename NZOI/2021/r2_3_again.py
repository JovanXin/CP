possible_days = 0
days = int(input())
r, p, d, g = map(int, input().split())

d_amounts = {"r": r, "p": p, "d": d, "g": g}

duck_each_day = [c for c in input()]

r_amounts = {
    "r": r - duck_each_day.count("R"),
    "p": p - duck_each_day.count("P"),
    "d": d - duck_each_day.count("D"),
}

for i, d in enumerate(duck_each_day):
    print(d_amounts)
    d = d.lower()

    if d in d_amounts.keys():
        if d_amounts[d] <= 0:
            break
        else:
            possible_days += 1
            d_amounts[d] -= 1
            r_amounts[d] -= 1

    elif d == ".":  # If he could have any duck
        max = 0
        curr_option = ""
        for type, amount in r_amounts.items():
            if amount >= max:
                curr_option = type
                max = amount

        if max == 0:
            break
        else:
            d_amounts[type] -= 1
            possible_days += 1
            r_amounts[type] -= 1


print(possible_days)
print(sum(d_amounts.values()))
