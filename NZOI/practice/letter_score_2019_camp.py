n = int(input())
output = []

for i in range(n):
    phrase = input()
    output.append(phrase)

char = input()

for p in output:
    print(p.count(char.lower()))