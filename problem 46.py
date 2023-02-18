"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a
square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from math import isqrt


def get_primes(n):
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    for p in range(2, n):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False

    return sieve


def is_goldbach(n):
    for prime in range(3, n, 2):
        if primes[prime]:

            for square_foundation in range(1, isqrt((n - prime) // 2) + 1):
                if n == prime + 2 * (square_foundation ** 2):
                    return True

    return False


limit = 10000
primes = get_primes(limit)

for odd_composite in range(3, limit, 2):
    if not primes[odd_composite]:

        if not is_goldbach(odd_composite):
            print(odd_composite)
            break

