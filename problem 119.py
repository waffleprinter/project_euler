"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3
= 12. Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have
a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""


def is_interesting(n, i):
    digit_sum = sum(int(i) for i in str(n))
    return digit_sum == i


powers = sorted([[i ** e, i, e] for e in range(2, 50) for i in range(2, 1001)])
k = 0

for p in powers:
    if is_interesting(p[0], p[1]):
        k += 1

        if k == 30:
            print(print(f"{p[0]},  {p[1]}^{p[2]}"))
