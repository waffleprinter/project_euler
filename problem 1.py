"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_divisible_by(n):
    p = target // n
    return n * (p * (p + 1)) // 2


target = 999

print(sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15))
