"""
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2,
... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal
product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence, for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in
the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""
import timeit
from math import sqrt, prod


def breakdown(n, min_divisor=2):
    components = []

    for i in range(min_divisor, int(sqrt(n)) + 1):
        if n % i == 0:
            components.append([i, n // i])

            div_breakdown = breakdown(n // i, i)

            if div_breakdown:
                for j in div_breakdown:
                    components.append([i] + j)

    return sorted(components, key=sum, reverse=True)


def get_smallest(k):
    for n in range(k if k > 4 else 4, k ** 2 + 1):  # ARBITRARY LIMIT
        for i in breakdown_dict[n]:
            if len(i) > k:
                continue

            if prod(i) == (k - len(i)) + sum(i):
                return n


breakdown_dict = {i: breakdown(i) for i in range(4, 13001)}

start = timeit.default_timer()

print(sum(set(get_smallest(k) for k in range(2, 12001))))
print(timeit.default_timer() - start)
