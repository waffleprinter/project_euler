"""
Too annoying lol, check the thing.
"""

from math import isqrt


def is_prime(n):
    if n < 1:
        return False

    if n == 2:
        return True

    if n == 1 or n % 2 == 0:
        return False

    for i in range(3, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True


primes = []

for i in range(1, 1000):
    if is_prime(i):
        primes.append(i)

n = 0
max_n = 0
ab_product = 0

for a in range(-999, 1000, 2):
    for b in primes:
        while is_prime(n*n + a*n + b):
            n += 1

        if n > max_n:
            max_n = n
            ab_product = a * b

        n = 0

print(ab_product)
