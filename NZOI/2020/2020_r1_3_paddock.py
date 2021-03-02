n = input()  # useless
y1 = list(map(int, input().split()))
n = input()
y2 = list(map(int, input().split()))
n = input()
y3 = list(map(int, input().split()))


def solve(y1, y2, y3):
    y1_avg = sum(y1) / len(y1)
    y2_avg = sum(y2) / len(y2)
    y3_avg = sum(y3) / len(y3)

    if y1_avg >= 12 and y2_avg >= 12 and y3_avg >= 12:
        if len([num for num in y1 if num >= 25]) >= (len(y1) / 2):
            print("resow")
            return
        else:
            print("unhealthy")
            return
    else:
        print("healthy")
        return


solve(y1, y2, y3)