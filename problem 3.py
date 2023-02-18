"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import isqrt

number = 600851475143

for i in range(2, isqrt(number) + 1):
    if number // i != 1:
        while number % i == 0:
            number //= i

print(number)
