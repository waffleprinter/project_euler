from math import log2
from fractions import Fraction


def generate_k_list(limit):
    k_list = []

    for a in range(2, limit):
        k_list.append(a * (a - 1))
        if k_list[-1] > limit:
            break

    k_list = k_list[0:-1]
    return k_list


def P(m):
    k_list = generate_k_list(m)
    a_list = [i for i in range(2, len(k_list) + 2)]

    return Fraction(int(log2(a_list[-1])), (a_list[-1] - 1))


#1/12345 so a[-1] >= 12345
#P(12345 * 12344) = 13/12345 so a[-1} >= 12345*13
#P(13*12345 * 13*12345-1) = 17/(13*12345) so a[-1} >= 12345*17
# that EQUALS, we need SMALLER
# so plus one

print(P(209867 * 209866))

