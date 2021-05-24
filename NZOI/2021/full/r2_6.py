h, w = map(int, input().split())
n = int(input())

grid = [[0] * h] * w

duck_locations = []

for i in range(n):
    [strides, *steps] = map(int, input().split())

    up = True
    x, y = 0, 0
    collusion = False

    for step in steps:
        if up:
            for other_x, other_y in duck_locations:
                if other_x == x:
                    if other_y >= y and other_y <= y + step:
                        collusion = True

            y += step

        else:
            for location in duck_locations:
                if other_y == y:
                    if other_x >= x and other_x <= x + step:
                        collusion = True
            x += step

        up = not up

    duck_locations.append((x, y))

    if collusion:
        print("OUCH")
    else:
        print("smooth swimming")

# If we can insert in sorted order, then the 'x' and the 'y' would be able to be checked faster