"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import isqrt


def is_prime(n):
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


number = 3
prime_key = 1

while prime_key != 10001:
    if is_prime(number):
        prime_key += 1

    number += 2

print(number)
