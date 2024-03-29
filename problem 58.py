"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that
8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this
process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals
first falls below 10%?
"""

from math import isqrt


def is_prime(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    if n % 3 == 0:
        return False

    for i in range(6, isqrt(n) + 1, 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False

    return True


primes = 3
total = 5

k = 4
num = 9

while 10 * primes > total:
    for i in range(4):
        num += k

        if i != 3:
            if is_prime(num):
                primes += 1

        total += 1

    k += 2

print(f"side length: {k - 1}")
