# Idea - generate all possible L shapes first then search for themselves

# New idea, start at each row / column and move forward until hit a 0

tc = int(input())

for t in range(1, tc + 1):
    grid = []
    num_rows, num_cols = map(int, input().split())
    for i in range(num_rows):
        grid.append(input().split())

    cols = [[] * num_cols]

    for i in range(len(grid)):
        print(f"{i=}{grid[i]=}")
        for j in range(len(grid[i])):
            print(f"{i=}{j=}{grid[i][j]=}")
            cols[j].append(grid[i][j])

    for col in cols:
        print(f"{col=}")

    for row in grid:
        current = 0
        max_current = 0
        for i in range(len(row)):
            if row[i] == "1":
                current += 1
            else:
                max_current = max(current, max_current)

            print(f"{row=}{max_current=}")

            # for j in range(i, len(row)):
            #     if row[j] == "1":
            #         current += 1
            #     else:
            #         break
            # print(f"{row=}{current=}")

    # print(f"Case #{t}: {ans}")