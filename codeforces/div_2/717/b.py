arr = [1, 2, 3 , 3, 3]


def xor(arr):
    new_arr = []
    for i in range(len(arr) - 3):
        new_arr.append(arr[i] ^ arr[i + 1])

    new_arr.append(arr[-2])
    new_arr.append(arr[-1])
    return new_arr


print(xor(arr))