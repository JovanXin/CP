"""
ISSUES THAT I HAD
- Read question incorrectly, assumed indexes started at 1 -> 10, instead of 0 -> 9
- forgot that once you read in input, it is "consumed" (while input() != "-1, -1" results in skipping over of an input)
"""

# Look in onenotes for your thinking

ship_locations = {}

for y in range(10):
    for x, char in enumerate(input().split()):
        if char != "#":
            ship_locations[(x, y)] = char

# Now we have coords of each ship

data = input()
while data != "-1 -1":
    x, y = map(int, data.split())

    if (x, y) in ship_locations:
        char = ship_locations[(x, y)]
        del ship_locations[(x, y)]

        if char not in ship_locations.values():
            print(f"Sunk {char}")
        else:
            print(f"Hit {char}")
    else:
        print("Miss")

    data = input()
