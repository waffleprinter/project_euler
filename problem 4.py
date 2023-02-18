"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest_palindrome = "0"

for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        product = str(i * j)

        if product == product[::-1]:
            if int(product) > int(largest_palindrome):
                largest_palindrome = product

print(largest_palindrome)
