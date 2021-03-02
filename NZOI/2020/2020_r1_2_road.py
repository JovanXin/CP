# Use the modulo operator I completely forgot about :|
facilities = list(map(int, input().split()))

distance = int(input())

distances = sorted(min(distance % x, x - distance % x) for x in facilities)

print(distances[0])
if distances[0] == distances[1]:
    print("can't make up my mind")