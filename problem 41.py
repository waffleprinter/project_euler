"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from math import isqrt
from itertools import permutations


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


for number_digits in ([7, 6, 5, 4, 3, 2, 1], [4, 3, 2, 1]):
    perms = permutations(number_digits)

    for perm in perms:
        perm = [str(digit) for digit in perm]
        int_perm = int("".join(perm))

        if is_prime(int_perm):
            print(int_perm)
            break


