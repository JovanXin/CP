tc = int(input())

for t in range(1, tc + 1):
    grid = []
    rows, cols = map(int, input().split())
    for i in range(rows):
        grid.append(input().split())