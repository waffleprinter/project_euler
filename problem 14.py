"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def get_terms(n):
    number_of_terms = 1

    while n != 1:
        if n % 2 == 0:
            n //= 2

        else:
            n = 3 * n + 1

        number_of_terms += 1

    return number_of_terms


most_terms = 0
the_number = 0

for i in range(1, 1000000):
    current_terms = get_terms(i)

    if current_terms > most_terms:
        most_terms = current_terms
        the_number = i

print(the_number)

