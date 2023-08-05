from itertools import product
from fractions import *


def get_probability_curve(possible_rolls: product) -> dict:
    probabilities = {}

    for roll in possible_rolls:
        roll_sum = sum(roll)

        if roll_sum in probabilities:
            probabilities[roll_sum] += 1
        else:
            probabilities[roll_sum] = 1

    total_possible_rolls = sum(i for i in probabilities.values())

    for roll, probability in probabilities.items():
        probabilities[roll] = Fraction(probability, total_possible_rolls)

    return probabilities


pyramidal_probability_curve = get_probability_curve(product([1, 2, 3, 4], repeat=9))
cubic_probability_curve = get_probability_curve(product([1, 2, 3, 4, 5, 6], repeat=6))

# cpbc = chance that pyramidal peter beats cubic colin
cpbc = Fraction(0, 1)

for pyramidal_roll in pyramidal_probability_curve.keys():
    for cubic_roll in range(list(cubic_probability_curve)[0], pyramidal_roll):
        cpbc += pyramidal_probability_curve[pyramidal_roll] * cubic_probability_curve[cubic_roll]

print(cpbc.numerator / cpbc.denominator)

# ROUND IT YOURSELF


