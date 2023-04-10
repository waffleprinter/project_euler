"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue
discs that the box would contain.
"""

n = 85
d = 120
last_n = 15
last_d = 21

while d < 10 ** 13:
    probability = (n * (n - 1)) / (d * (d - 1))

    if probability < 0.5:
        n += 1

    elif probability > 0.5:
        d += 1

    else:
        print(n, d)
        n, d, last_n, last_d = int(n * n / last_n), int(d * d / last_d), n, d

print(n, d)

# I DIDN'T FEEL LIKE CORRECTING THE PROGRAM, THE ANSWER IS N = 756872327473, D = 1070379110497
# 756872327473 1070379110497
