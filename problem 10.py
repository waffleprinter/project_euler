"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def get_prime_sum(n):
    sieve = [True] * n
    sum_of_primes = 2

    for p in range(3, n, 2):
        if sieve[p]:
            sum_of_primes += p

            for i in range(p * p, n, p):
                sieve[i] = False

    return sum_of_primes


print(get_prime_sum(2000000))

