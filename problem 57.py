"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
sqrt(2) = I can't write this
By expanding this for the first four iterations, we get:


The next three expansions are
99/70,
239/169, and
577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the
denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

answer = 0
numerator = 3
denominator = 2

for i in range(1000):
    if len(str(numerator)) > len(str(denominator)):
        answer += 1

    numerator, denominator = 2 * denominator + numerator, numerator + denominator

print(answer)
