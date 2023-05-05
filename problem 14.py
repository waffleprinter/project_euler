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
import timeit


def collatz(n):
    if n == 1:
        return 1

    if n in collatz_dictionary:
        return collatz_dictionary[n]

    new = collatz(n // 2) + 1 if n % 2 == 0 else collatz(n * 3 + 1) + 1
    collatz_dictionary[n] = new

    return new


collatz_dictionary = {}

longest_chain = 0
corresponding_starting_number = None

for i in range(1, 1000000):
    chain_length = collatz(i)

    if chain_length > longest_chain:
        longest_chain = chain_length
        corresponding_starting_number = i

print(corresponding_starting_number, longest_chain)
