"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from math import isqrt


def has_four_dpf(n):
    distinct_prime_factors = 0

    if n % 2 == 0:
        distinct_prime_factors += 1

        while n % 2 == 0:
            n //= 2

    for i in range(3, isqrt(n), 2):
        if n % i == 0:
            distinct_prime_factors += 1

            if distinct_prime_factors == 5:
                return False

            while n % i == 0:
                n //= i

    if n > 2:
        distinct_prime_factors += 1

    return distinct_prime_factors == 4


not_found = True
number = 1

while not_found:
    number += 2

    if has_four_dpf(number):
        if has_four_dpf(number - 1):
            if has_four_dpf(number + 1) and has_four_dpf(number + 2):
                print(number - 1)
                not_found = False

        elif has_four_dpf(number + 1):
            if has_four_dpf(number + 2) and has_four_dpf(number + 3):
                print(number)
                not_found = False
