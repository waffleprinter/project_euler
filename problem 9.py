"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt


def get_triplet_product(target):
    for a in range(1, target):
        for b in range(a, target):
            c = sqrt(a ** 2 + b ** 2)

            if a + b + c == target:
                return int(a * b * c)


print(get_triplet_product(1000))
