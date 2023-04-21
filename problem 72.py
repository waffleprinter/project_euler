"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

from math import prod
from itertools import combinations

limit = 1000000
prime_factor_dict = {i: [] for i in range(1, limit + 1)}
count = limit ** 2 - 1

for n in range(2, limit + 1):
    if prime_factor_dict[n]:
        continue

    for j in range(n, limit + 1, n):
        prime_factor_dict[j].append(n)

for n in range(2, limit + 1):
    count -= n
    all_combinations = []

    for i in range(1, len(prime_factor_dict[n]) + 1):
        for j in list(combinations(prime_factor_dict[n], i)):
            all_combinations.append(j)

    for comb in all_combinations:
        if len(comb) % 2 != 0:
            count -= (limit - n) // (prod(comb))

        else:
            count += (limit - n) // (prod(comb))

print(count)
