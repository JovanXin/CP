h, w = map(int, input().split())
num_ducks = int(input())

width = [0] * w
height = [0] * h

for i in range(num_ducks):
    location = 0
    route = list(map(int, input().split()))
    route_w = route[2::2]
    route_h = route[1::2]

    if (
        width[sum(route_w) - 1] == 1 and width[sum(route_h) - 1] == 1
    ):  # already a duck in that location
        print("OUCH")
    else:
        width[sum(route_w) - 1] = 1
        height[sum(route_w) - 1] = 1

        if sum(width[: sum(route_w) - 1]) == 0 and sum(height[: sum(route_h) - 1]) == 0:
            print("smooth swimming")
        else:
            print("OUCH")
