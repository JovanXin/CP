import math


def get_primes(n):
    # Uses a sieve to get all the primes, ran into memory issues though
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * int(((n - i * i - 1) / (2 * i) + 1))
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


primes = get_primes(100000)

tc = int(input())

for t in range(1, tc + 1):
    smallest_diff = float("inf")
    z = int(input())

    for i in range(len(primes) - 1):
        if primes[i] * primes[i + 1] > z:
            break
        elif z - (primes[i] * primes[i + 1]) < smallest_diff:
            smallest_diff = z - (primes[i] * primes[i + 1])
            smallest_vals = [primes[i], primes[i + 1]]

    print(f"Case #{t}: {z - smallest_diff}")
