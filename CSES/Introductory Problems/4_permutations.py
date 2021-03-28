n = int(input())

solution = []

if n == 1:
    print(1)
elif n > 3:
    if n == 4:
        print(*[2, 4, 1, 3], sep=" ")
    else:
        for i in range(1, n + 1, 2):
            solution.append(i)

        for i in range(2, n + 1, 2):
            solution.append(i)

        print(*solution, sep=" ")
else:
    print("NO SOLUTION")
