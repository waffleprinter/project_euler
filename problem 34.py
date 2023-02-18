"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

total_sum = 0

for i in range(10, 3265920):
    if i == sum(factorial(int(digit)) for digit in str(i)):
        total_sum += i

print(total_sum)
