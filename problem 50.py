"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

# i am so sorry

import timeit
start = timeit.default_timer()


def find_primes(n):
    sieve = [True] * n
    prime_lst = [2]

    for p in range(4, n, 2):
        sieve[p] = False

    for p in range(3, n, 2):
        if sieve[p]:
            prime_lst.append(p)

            for i in range(p * p, n, p):
                sieve[i] = False

    return prime_lst


prime_list = find_primes(1000000)
prime_dict = {}

for num in prime_list:
    prime_dict[num] = True


starting_num = 0
max_terms = 1
the_prime = 0

while starting_num < len(prime_list) / max_terms:
    current_sum = 0
    i = starting_num

    while i < len(prime_list):
        current_sum += prime_list[i]
        i += 1

        if current_sum in prime_dict:
            if i - starting_num > max_terms:
                max_terms = i - starting_num
                the_prime = current_sum

    starting_num += 1

print(the_prime)

print(timeit.default_timer() - start)
