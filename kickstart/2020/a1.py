tc = int(input())

for t in range(1, tc + 1):
    str_len, wanted_g = map(int, input().split())

    string = list(input())

    goodness = 0

    for c in range(int(str_len / 2)):
        if string[c] != string[str_len - (c + 1)]:
            goodness += 1

    print(
        f"Case #{t}: {abs(wanted_g - goodness)}"
    )  # REMEMBER TO USE THE FUCKING ABSOLUTE VALUE
