from math import log10, floor


def ending_is_pandigital(n):
    last_nine_digits = n % (10 ** 9)
    unique_digits = set()

    while last_nine_digits > 0:
        unique_digits.add(last_nine_digits % 10)
        last_nine_digits //= 10

    if 0 in unique_digits:
        return False

    return len(unique_digits) == 9


def beginning_is_pandigital(n):
    first_nine_digits = n // (10 ** floor(log10(n) - 8))
    unique_digits = set()

    while first_nine_digits > 0:
        unique_digits.add(first_nine_digits % 10)
        first_nine_digits //= 10

    if 0 in unique_digits:
        return False

    return len(unique_digits) == 9


a = 1
b = 1
c = a + b
index = 3

while True:
    if ending_is_pandigital(c):
        if beginning_is_pandigital(c):
            print(index)
            break

    a = b
    b = c
    c = a + b
    index += 1
