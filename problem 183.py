from fractions import Fraction
from math import e
from timeit import default_timer


def is_terminating(denominator):
    while denominator % 2 == 0:
        denominator //= 2

    while denominator % 5 == 0:
        denominator //= 5

    return denominator == 1


def P(N, k):
    return Fraction(N, k) ** k


def M(N):
    k_candidates = list(map(lambda x: 1 if x == 0 else x, [int(N / e) + i for i in range(-1, 2)]))

    return max(P(N, k) for k in k_candidates)


def D(N):
    return -N if is_terminating(M(N).denominator) else N


def T(lim):
    return sum(D(N) for N in range(5, lim + 1))


start = default_timer()
print(T(10000))
print(default_timer() - start)
