pets = list(map(int, input().split()))
print(f"Pet {pets.index(max(pets)) + 1}")