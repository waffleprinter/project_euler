"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import timeit


def get_reversed(n):
    reversed_number = 0

    while n != 0:
        reversed_number = reversed_number * 10 + n % 10
        n //= 10

    return reversed_number


largest_palindrome = 0

for i in range(1000, 100, -1):
    for j in range(i, 100, -1):
        product = i * j

        if product < largest_palindrome:
            break

        if product == get_reversed(product):
            if product > largest_palindrome:
                largest_palindrome = product

print(largest_palindrome)
