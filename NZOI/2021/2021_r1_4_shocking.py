"""
This was kinda the idea I was going for during the contest, however the 'efficency' of the hurt 
also needs to include the cost of each time you press the '=' button...

There's also probably some issues with the indexes (struggling with those quite a bit, when to +1/leave it alone)
Should honestly just change them all at the start or the end.
"""

price = int(input())
max_price = price

total_hurt = 0

hurt_value_nums = list(map(int, input().split()))
hurt_value_symbols = list(map(int, input().split()))

symbols = {
    "+": hurt_value_symbols[0],
    "*": hurt_value_symbols[1],
    "=": hurt_value_symbols[2],
}

efficent = []
min_efficency = max(hurt_value_nums)

for num in range(len(hurt_value_nums)):
    hurt = hurt_value_nums[num]
    if num > 0:
        efficency = hurt / num
        efficent.append(efficency)

min = min(efficent)
num = efficent.index(min)

efficency_dict = {
    num + 1: efficent for num, efficent in enumerate(efficent) if efficent == min
}

times = 0

while max_price > 0:
    if max_price - (num + 1) < 0:
        break
    times += 1
    max_price -= num + 1

hurt = (
    (times * hurt_value_nums[num + 1]) + ((times - 1) * (symbols["+"])) + symbols["="]
)

if max_price > 0:
    hurt += hurt_value_nums[max_price]
    hurt += symbols["+"]

print(f"Hurt is {hurt}")  # Yeah this doesn't work at all
