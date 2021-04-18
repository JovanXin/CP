possible_days = 0
days = int(input())
r, p, d, g = map(int, input().split())

d_amounts = {"r": r, "p": p, "d": d, "g": g}

duck_each_day = [c.lower() for c in input()]


for i, d in enumerate(duck_each_day):
    d = d.lower()

    if d in d_amounts.keys():
        if d_amounts[d] <= 0:
            break
        else:
            possible_days += 1
            d_amounts[d] -= 1

    elif d == ".":  # If he could have any duck
        rmr = d_amounts["r"] - duck_each_day[i:].count("r")
        rmp = d_amounts["p"] - duck_each_day[i:].count("p")
        rmd = d_amounts["d"] - duck_each_day[i:].count("d")

        remainders = {"r": rmr, "p": rmp, "d": rmd}
        max_remainders = {}

        # OPTIMIZATION FOR THE FURTHEST INDEX AWAY
        for type, amount in remainders.items():
            if amount == max(remainders.values()):
                if type in duck_each_day[i:]:
                    max_remainders[duck_each_day[i:].index(type)] = type
                else:
                    max_remainders[500001] = type

        # HOW DO I GET THE KEY FROM THE VALUE? THE VALUE IS THE INDEX THAT I WANT
        type_to_use = max_remainders[max(max_remainders.keys())]

        if d_amounts[type_to_use] > 0:
            d_amounts[type_to_use] -= 1
            possible_days += 1
        else:
            break

print(possible_days)
print(sum(d_amounts.values()))
