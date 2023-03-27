"""
Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

It is not a palindrome, and
It is the square of a prime, and
Its reverse is also the square of a prime.
169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.


"""
from math import sqrt, isqrt


def get_primes(n):
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, isqrt(n) + 1, 2):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False

    return sieve


def is_palindromic(n):
    str_n = str(n)
    return str_n == str_n[::-1]


n = 100000000
primes = get_primes(n)
count = 0
total_sum = 0

for i in range(n):
    if primes[i]:
        i_squared = i ** 2

        if not is_palindromic(i_squared):
            reversed_i_squared = int(str(i_squared)[::-1])
            reversed_i_squared_root = sqrt(reversed_i_squared)

            if reversed_i_squared_root.is_integer():
                if primes[int(reversed_i_squared_root)]:
                    count += 1
                    total_sum += i_squared

                    if count == 50:
                        break

print(total_sum)
