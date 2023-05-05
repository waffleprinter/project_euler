"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt
import timeit


def get_primes(n):
    sieve = [True] * n

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, int(sqrt(n)) + 1, 2):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False

    return sieve


limit = 2000000

primes = get_primes(limit)
prime_sum = 2

for i in range(3, limit, 2):
    if primes[i]:
        prime_sum += i

print(prime_sum)
