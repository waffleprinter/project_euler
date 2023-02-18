"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


def find_primes(n):
    sieve = [True] * n
    prime_list = []

    for p in range(2, n):
        if sieve[p]:
            prime_list.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False

    return prime_list


def good_filter(n):
    good_nums = {"1", "3", "7", "9"}

    if not set(str(n)).difference(good_nums):
        return True

    return False


def rotate(n):
    return str(n)[1:] + str(n)[0]


def is_circular(n, lst):
    for x in range(len(str(n)) - 1):
        n = rotate(n)

        if int(n) not in lst:
            return False

    return True


primes = tuple(filter(good_filter, find_primes(1000000)))
circular_primes = 2

for i in primes:
    if is_circular(i, primes):
        circular_primes += 1

print(circular_primes)
