vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvxqyz"

wl = int(input())
w = input()
translations = 0

word = w.replace("onk", "")

for char in word:
    if char in vowels:
        word = w.replace(f"lf{char}", "")

print(word)
