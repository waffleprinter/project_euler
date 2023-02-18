"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i)
each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one
other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from itertools import permutations


def get_primes(n):
    sieve = [True] * n
    prime_dictionary = {}

    for p in range(4, n, 2):
        sieve[p] = False

    for p in range(3, n, 2):
        if sieve[p]:
            if p > 999:
                prime_dictionary[p] = True

            for i in range(p * p, n, p):
                sieve[i] = False

    return prime_dictionary


primes = get_primes(10000)

for prime in primes:
    prime_perms = set()

    for perm in permutations(str(prime)):
        int_perm = int("".join(perm))

        if int_perm in primes:
            prime_perms.add(int_perm)

    for prime_perm in prime_perms:
        if prime_perm > prime:
            difference = abs(prime - prime_perm)

            if prime + 2 * difference in prime_perms:
                concatenated = int(str(prime) + str(prime_perm) + str(prime_perm + difference))

                if concatenated != 148748178147:
                    print(concatenated)
