from math import sqrt


def get_primes(n):
    sieve = [True] * n
    prime_list = [0, 2]

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, n, 2):
        if sieve[p]:
            prime_list.append(p)

            for i in range(p * p, n, p):
                sieve[i] = False

    return prime_list


p = get_primes(1000000)
limiter = 10 ** 10

for n in range(7039, len(p), 2):
    if not p[n]:
        continue

    if ((p[n] - 1) ** n + (p[n] + 1) ** n) % (p[n] ** 2) > 10 ** 10:
        print(n)
        break
