"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def get_primes(n):
    sieve = [True] * n
    prime_dict = {2: True}

    for p in range(4, n, 2):
        sieve[p] = False

    for p in range(3, n, 2):
        if sieve[p]:
            prime_dict[p] = True
            for i in range(p * p, n, p):
                sieve[i] = False

    return prime_dict


def find_truncated(n):
    truncations = []
    n = str(n)

    for i in range(1, len(n)):
        truncations.append(int(n[i:]))
        truncations.append(int(n[:-i]))

    return truncations


def is_truncatable(n):
    for truncation in find_truncated(n):
        if truncation not in primes:
            return False

    return True


primes = get_primes(1000000)
total_sum = 0

for prime in primes:
    if prime not in [2, 3, 5, 7]:
        if is_truncatable(prime):
            total_sum += prime

print(total_sum)
