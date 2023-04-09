"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there
are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

from math import isqrt


def get_primes(n):
    sieve = [True] * n
    prime_list = [2]

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, n, 2):
        if sieve[p]:
            prime_list.append(p)

            for i in range(p * p, n, p):
                sieve[i] = False

    return prime_list


primes = get_primes(isqrt(50000000) + 1)
valid_numbers = set()

for fourth_root in primes:
    fourth = fourth_root ** 4

    for cube_root in primes:
        cube = cube_root ** 3

        for square_root in primes:
            square_cube_fourth_sum = square_root ** 2 + cube + fourth

            if square_cube_fourth_sum < 50000000:
                valid_numbers.add(square_cube_fourth_sum)

            else:
                break

print(len(valid_numbers))

# THIS IS SUCH A LAZY SOLUTION IM SO SORRY
