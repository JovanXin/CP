x_lv, y_lv = map(int, input().split())
x_rv, y_rv = map(int, input().split())

print((abs(x_lv - x_rv) * 2) + abs(y_lv - y_rv) * 2)
