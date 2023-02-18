"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n, and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt, isqrt


def classification(n):
    sum_proper_divisors = 1

    for x in range(2, round(sqrt(n)) + 1):
        if n % x == 0:
            sum_proper_divisors += x + n / x

    if isqrt(n) ** 2 == n:
        sum_proper_divisors -= sqrt(n)

    if sum_proper_divisors > n:
        return 1

    elif sum_proper_divisors == n:
        return 0

    else:
        return -1


def is_abundant_summable(n):
    a = 0
    b = n

    while a <= b:
        if table[a] == 1 and table[b] == 1:
            return True

        a += 1
        b -= 1

    return False


table = []

for i in range(1, 28124):
    table.append(classification(i))

total_sum = 0

for i in range(28124):
    if not is_abundant_summable(i):
        total_sum += i

print(total_sum)

