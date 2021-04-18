# Only 60%, unoptimized

NUM_TO_SOLVE = 5


def unoptimized(num):
    string = ""
    for i in range(1, num + 1):
        string += str(i)

    num_three = string.count("3")
    return num_three


def optimized(num):
    """
    We will break the number down into invidiaul components
    1320 -> 1000, 300, 200, then we check each individual number to see how many 3's
    """
    ans = 0

    for i in range(len(num)):
        d = int(num[i])  # The current digit, going from highest to lowest

        if d == 3:
            print("D IS 3")
            ans += int("0" + num[i + 1]) + 1

    return ans


def the_solution(num):
    ans = 0
    for i in range(len(num)):
        d = int(num[i])  # The current digit
        j = len(num) - i - 1
        sj = j * (10 ** j) // 10
        ans += d * sj

        if d == NUM_TO_SOLVE:
            ans += int("0" + num[i + 1 :]) + 1
        elif d > NUM_TO_SOLVE:
            ans += 10 ** j

    return ans


num = input()
print(the_solution(num))
print(unoptimized(int(num)))
