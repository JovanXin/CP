tc = int(input())

for w in range(1, tc + 1):
    sl = int(input())
    string = [ord(c) for c in input()]

    dp = [1] * sl
    counter = 1

    for i in range(1, sl):
        if string[i] <= string[i - 1]:
            counter = 1
        else:
            counter += 1
            dp[i] = counter

    print(f"Case #{w}: {' '.join(str(x) for x in dp)}")