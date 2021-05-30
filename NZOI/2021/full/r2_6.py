import bisect


# Full binary search unneeded
def binary_search(arr, axis, step):
    # print("FUNCTION CALLED")
    start = 0
    end = len(arr)
    middle = start + (end - start) // 2

    while start <= end:
        middle = start + (end - start) // 2
        # print(f"start: {start}, mid: {middle}, end: {end}")
        if middle >= len(arr):
            return False
        if arr[middle] >= axis:
            if arr[middle] <= axis + step:
                # print(f"index {middle} is {arr[middle]} and is lte  {axis+step}")
                return True
            else:
                end = middle - 1
        else:
            start = middle + 1
    return False


# print(binary_search([1, 5, 6, 36, 245, 2356, 23512], 23513, 23513))

h, w = map(int, input().split())
n = int(input())
message = ""

grid = [[0] * h] * w

columns = {}
rows = {}

for i in range(n):
    [strides, *steps] = map(int, input().split())

    up = True
    x, y = 0, 0
    collusion = False

    for step in steps:
        if up:
            if x in columns and not collusion:
                position = bisect.bisect_left(columns[x], y)
                if position != len(columns[x]):
                    val = columns[x][position]
                    if val >= y and val <= y + step:
                        collusion = True

            y += step

        else:
            if y in rows and not collusion:
                position = bisect.bisect_left(rows[y], x)
                if position != len(rows[y]):
                    val = rows[y][position]
                    if val >= x and val <= x + step:
                        collusion = True

            y += step

        up = not up  # Switches the direction the duck travels in

    # Should insert in asecending order

    if x not in columns:
        columns[x] = []
    if y not in rows:
        rows[y] = []

    bisect.insort(columns[x], y)
    bisect.insort(rows[y], x)

    if collusion:
        message += "OUCH\n"
    else:
        message += "smooth swimming\n"

print(message)
