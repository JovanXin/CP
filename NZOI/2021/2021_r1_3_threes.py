# Only 60%, unoptimized


def unoptimized(num):
    string = ""
    for i in range(1, num + 1):
        string += str(i)

    num_three = string.count("3")
    return num_three


def optimized(num):
    return 3 * (num ^ (num - 1))


num = int(input())
print(unoptimized(num))
print(optimized(num))