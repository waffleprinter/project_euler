"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


def simplify_incorrectly(n, d):
    numerator = str(n)
    denominator = str(d)

    overlapping_digits = set(numerator).intersection(set(denominator))

    if len(overlapping_digits) == 0:
        return None

    for digit in overlapping_digits:
        numerator = numerator.replace(digit, "", 1)
        denominator = denominator.replace(digit, "", 1)

    if len(numerator) == 0 or len(denominator) == 0:
        return None

    if denominator == "0":
        return None

    return int(numerator) / int(denominator)


product = 1

for num in range(10, 100):
    for den in range(num + 1, 100):
        if num % 10 == 0 and den % 10 == 0:
            continue

        if num / den == simplify_incorrectly(num, den):
            product *= num / den

print(product)



