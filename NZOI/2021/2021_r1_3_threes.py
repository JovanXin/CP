# Only 60%, unoptimized


def unoptimized(num):
    string = ""
    for i in range(1, num + 1):
        string += str(i)

    num_three = string.count("3")
    return num_three


def optimized(num):
    return


num = int(input())
print(unoptimized(num))
print(optimized(num))