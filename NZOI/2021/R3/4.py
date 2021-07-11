"""
100/100
Issues faced
1) Initially, misunderstood how to handle the comparison between two lists
    -> Solved by taking a break lol
"""
total = 0
customers = int(input())
customer_bids = [int(input()) for bid in range(customers)]
number_of_j_phones = int(input())
j_phone_prices = [int(input()) for phone in range(number_of_j_phones)]



customer_bids.sort()
customer_bids.reverse()
j_phone_prices.sort()
j_phone_prices.reverse()

purchases = 0
i = 0
while True:
    if i >= len(j_phone_prices) or purchases >= len(customer_bids):
        break
    if customer_bids[purchases] >= j_phone_prices[i]:
        total += j_phone_prices[i]
        purchases += 1
        i += 1
    else:
        i += 1

print(total)