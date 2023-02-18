"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt, isqrt


def d(n):
    if n == 1:
        return 0

    sum_proper_divisors = 1

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            sum_proper_divisors += i + n // i

    if n % sqrt(n) == 0:
        sum_proper_divisors -= isqrt(n)

    return sum_proper_divisors


amicable_numbers = []

for a in range(2, 10001):
    b = d(a)

    if d(b) == a and a != b and a < b:
        amicable_numbers.extend([a, b])

print(sum(amicable_numbers))