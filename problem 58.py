from math import isqrt


def is_prime(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    if n % 3 == 0:
        return False

    for i in range(6, isqrt(n) + 1, 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False

    return True


primes = 3
total = 5

k = 4
num = 9

while 10 * primes > total:
    for i in range(4):
        num += k

        if i != 3:
            if is_prime(num):
                primes += 1

        total += 1

    k += 2

print(f"side length: {k - 1}")
