"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def is_perm(n, var):
    n_set = set([digit for digit in str(n)])
    var_set = set([digit for digit in str(var)])

    return n_set == var_set


number = 0
not_found = True

while not_found:
    number += 1

    for multiplier in range(2, 7):
        if not is_perm(number, number * multiplier):
            break

        if multiplier == 6:
            not_found = False

print(number)
