"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def is_decimal_palindrome(n):
    return True if int(str(n)[::-1]) == n else False


def is_binary_palindrome(n):
    binary_number = bin(n).replace("0b", "")

    return True if int(binary_number[::-1]) == int(binary_number) else False


decimal_binary_palindromes = []

for i in range(1, 1000000):
    if is_decimal_palindrome(i):
        if is_binary_palindrome(i):
            decimal_binary_palindromes.append(i)

print(decimal_binary_palindromes)
print(sum(decimal_binary_palindromes))
