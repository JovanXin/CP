"""
20/100
A quick, hacky solution to grab the first testcase.
I'm not familiar with graphs/trees so decided to try focus on other questions
"""
n, d = map(int, input().split())
for i in range(n-1):
    a, b = map(int, input().split())

spies = [[i, True] for i in range(n)]


print(n)
comprimised_chain = n

for days in range(d):
    comprimised = int(input())
    comprimised_chain = min(comprimised_chain, comprimised)
    print(comprimised_chain)



