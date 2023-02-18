"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def recurring_cycle_length(d):
    n = 10
    decimals = ""

    while n / d < 1:
        n *= 10
        decimals += "0"

    used_ns = []
    is_not_periodic = True

    while is_not_periodic:
        if n / d < 1:
            n *= 10

        if n not in used_ns:
            used_ns.append(n)
            decimals += str(n // d)
            n %= d

            if n == 0:
                is_not_periodic = False

        else:
            return len(decimals) - used_ns.index(n)

    return 0


max_recurring_cycle_length = 0
max_i = 0

for i in range(2, 1000):
    if recurring_cycle_length(i) > max_recurring_cycle_length:
        max_recurring_cycle_length = recurring_cycle_length(i)
        max_i = i

print(max_i)

