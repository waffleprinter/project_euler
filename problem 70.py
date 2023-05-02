"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers
less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""
import timeit
from math import sqrt, prod
from itertools import combinations


def phi(n):
    if not prime_factor_dictionary[n]:
        return n - 1

    count = n

    for k in range(1, len(prime_factor_dictionary[n]) + 1):
        for comb in combinations(prime_factor_dictionary[n], k):
            count += (n // prod(comb)) if k % 2 == 0 else -(n // prod(comb))

    return count


def is_permutation(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


limit = 10 ** 7
prime_factor_dictionary = {i: [] for i in range(1, limit + 1)}

for p in range(2, int(sqrt(limit)) + 1):
    if not prime_factor_dictionary[p]:
        for i in range(2 * p, limit, p):
            prime_factor_dictionary[i].append(p)

for p in range(int(sqrt(limit)), limit // 2 + 1):
    if not prime_factor_dictionary[p]:
        for i in range(2 * p, limit, p):
            prime_factor_dictionary[i].append(p)

lowest_quotient = 10000000000000
corresponding_n = None

for n in range(2, limit + 1):
    phi_of_n = phi(n)

    if is_permutation(n, phi_of_n):
        if n / phi_of_n < lowest_quotient:
            lowest_quotient = n / phi_of_n
            corresponding_n = n

print(f"\n{corresponding_n}, {lowest_quotient}")
