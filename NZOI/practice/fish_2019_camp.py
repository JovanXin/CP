"""
Use of modulo operations to reduce final answer

- Don't really know how to do lmao (apparently u can use before dividing/stuff?)
"""


def ii(m=None):
    if m:
        return list(map(int, input().split()))
    else:
        return int(input())


num_fish = ii()
gemstone_types = ii()
modulo = ii()

fishes = {}


for i in range(num_fish):
    fishy_length, stone_type = ii(True)

    # if stone_type in fishes.keys():
    #     if fishy_length < fishes[stone_type]:
    #         fishes[stone_type] = fishy_length

    fishes[stone_type] = fishy_length


for stone, length in fishes.items():
    possible = []
    for s2, l2 in fishes.items():
        if l2 >= length * 2:
            possible.append(s2)

    print(f"stone: {stone}possible: {possible}")
