# Only 60%, unoptimized
string = ""
num = int(input())

for i in range(1, num + 1):
    string += str(i)

num_three = string.count("3")

print(num_three)
