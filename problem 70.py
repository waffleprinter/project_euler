"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers
less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""
import timeit
from math import isqrt

start = timeit.default_timer()


def get_prime_factors(n):
    prime_factors = []

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            prime_factors.append(i)

            while n % i == 0:
                n //= i

    if n != 1:
        prime_factors.append(n)

    return prime_factors


def phi(n):
    if n == 1:
        return 1

    prime_factors = get_prime_factors(n)

    if prime_factors[0] == n:
        return n - 1

    sieve = [True] * n

    for p in prime_factors:
        for i in range(p, n, p):
            sieve[i] = False

    return sieve.count(True) - 1  # MINUS ONE FOR THE ZERO


n_over_phi_n_dict = {1: 1}

for i in range(2, 10000):
    if i in n_over_phi_n_dict:
        continue

    p = phi(i)
    e = 1
    power = i ** e
    n_over_phi_n = i / p

    while power < 1000000:
        n_over_phi_n_dict[power] = [power * p // i, n_over_phi_n]
        e += 1
        power = i ** e


for n in n_over_phi_n_dict.items():
    print(n)

print(timeit.default_timer() - start)
