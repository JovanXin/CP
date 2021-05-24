# proper implementation
days = int(input())
r, p, d, g = map(int, input().split())
wanted = input()


ducks = {"r": r, "p": p, "d": d, "g": g}  # Probably shouldn't include geese here?

days = 0
owed = 0

for day in wanted:
    day = day.lower()

    if owed >= sum(ducks.values()) - ducks["g"]:
        break
    elif day != ".":
        if ducks[day] > 0:
            ducks[day] -= 1
            days += 1
        else:
            break
    elif day == ".":
        if owed + 1 > sum(ducks.values()) - ducks["g"]:
            break
        else:
            owed += 1
            days += 1

print(days)
print(sum(ducks.values()) - owed)
