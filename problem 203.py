from math import sqrt


def factor(n):
    if n in factor_dict:
        return factor_dict[n]

    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            factor_dict[n] = factor(n // d) + factor(d)
            return factor_dict[n]

    factor_dict[n] = [n]
    return [n]


def factorial(n):
    ans = 1

    for i in range(2, n + 1):
        ans *= i

    return ans


def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def is_squarefree(n):
    factors = factor(n)

    return len(set(factors)) == len(factors)


factor_dict = {}
squarefree_set = set()

for n in range(51):
    for k in range(n // 2 + 1):
        value = choose(n, k)

        if is_squarefree(value):
            squarefree_set.add(value)

print(sum(squarefree_set))
