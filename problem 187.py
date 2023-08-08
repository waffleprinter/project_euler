from math import sqrt


def get_primes(n):
    sieve = [True] * n
    sieve[0], sieve[1] = False, False

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, int(sqrt(n)), 2):
        if sieve[p]:
            for i in range(p ** 2, n, p):
                sieve[i] = False

    return sieve


limit = 10 ** 8 - 1
primes = get_primes(limit // 2)
ans = 0

for i in range(2, int(sqrt(limit)) + 1):
    if primes[i]:
        ans += primes[i+1:limit//i+1].count(True) + 1

print(ans)


