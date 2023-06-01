"""
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares:
6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of
these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares
of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive
squares.
"""

from math import sqrt


def is_palindromic(n):
    return str(n) == str(n)[::-1]


limit = 10 ** 8
consecutive_sums = set()

for i in range(1, int(sqrt(limit) // 2)):
    num = i ** 2

    while num + (i + 1) ** 2 < limit:
        i += 1
        num += i ** 2
        consecutive_sums.add(num)

print(sum(i for i in consecutive_sums if is_palindromic(i)))
