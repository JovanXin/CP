price = int(input())
max_price = price

total_hurt = 0

hurt_value_nums = list(map(int, input().split()))
hurt_value_symbols = list(map(int, input().split()))

symbols = {
    "+": hurt_value_symbols[0],
    "*": hurt_value_symbols[1],
    "=": hurt_value_symbols[2]
}

number = {}

min_hurt = 0

for i in range(len(hurt_value_nums)):
    if i != 0:
        times = max_price / i
        hurt = times * hurt_value_nums[i] 

        if hurt < :
            min_hurt = i

print(number)




print(val)

print(total_hurt)
print(max_price)
