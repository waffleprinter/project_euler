import timeit
from math import sqrt, log


'''for first_prime in range(2, int(sqrt(limit))):
    if not primes[first_prime]:
        continue

    for first_prime_exponent in range(1, int(log(limit, first_prime))):
        first_power = first_prime ** first_prime_exponent

        for second_prime in range(first_prime + 1, int(limit / first_power)):
            if not primes[second_prime]:
                continue

            for second_prime_exponent in range(1, int(log(limit, second_prime))):
                second_power = second_prime ** second_prime_exponent

                try:
                    m_list[first_power * second_power] += 1
                    print(first_power, second_power)
                except IndexError:
                    print(first_power, second_power, 'ERROR')

print(m_list)
'''


def get_primes(n):
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, int(sqrt(n)) + 1, 2):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False

    return sieve


limit = 10 ** 7

primes = get_primes(limit + 1)
m_list = dict()

for first_prime in range(2, int(sqrt(limit))):
    if not primes[first_prime]:
        continue

    for second_prime in range(first_prime + 1, int(limit / first_prime) + 1):
        if not primes[second_prime]:
            continue

        for first_prime_exponent in range(1, int(log(limit / second_prime, first_prime)) + 1):
            first_power = first_prime ** first_prime_exponent

            for second_prime_exponent in range(1, int(log(limit / first_power, second_prime)) + 1):
                second_power = second_prime ** second_prime_exponent

                product = first_power * second_power

                if (first_prime, second_prime) not in m_list or product > m_list[(first_prime, second_prime)]:
                    m_list[(first_prime, second_prime)] = product

print(sum(m_list.values()))
