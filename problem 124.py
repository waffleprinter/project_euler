from math import sqrt, prod


def rad(n):
    distinct_prime_factors = set()

    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            distinct_prime_factors.add(i)
            n //= i

    return prod(distinct_prime_factors | {n}) if distinct_prime_factors else n


nums = [i for i in range(1, 100001)]
rads = [rad(i) for i in range(1, 100001)]

sorted_by_rads = [x for _, x in sorted(zip(rads, nums))]

print(sorted_by_rads[9999])
