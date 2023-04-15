"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28
are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a
chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

from math import sqrt


def get_proper_divisors_sum(n):
    if n < 2:
        return 0

    proper_divisor_sum = 1
    root_n = sqrt(n)

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            proper_divisor_sum += i + n // i

    if n % root_n == 0:
        proper_divisor_sum -= int(root_n)

    return proper_divisor_sum


limit = 1000000

amicable_array = [0] * limit
amicable_array[0] = -1

for starting_index in range(limit):
    if amicable_array[starting_index] == -1:
        continue

    current_index = starting_index
    current_chain_indices = []

    while current_index < limit and amicable_array[current_index] == 0 and current_index not in current_chain_indices:
        current_chain_indices.append(current_index)
        current_index = get_proper_divisors_sum(current_index)

    if current_index >= limit:
        for i in current_chain_indices:
            amicable_array[i] = -1

    elif current_index == starting_index:
        for i in current_chain_indices:
            amicable_array[i] = len(current_chain_indices)

    elif amicable_array[current_index] == -1:
        for i in current_chain_indices:
            amicable_array[i] = -1

    elif current_index in current_chain_indices:
        for i in current_chain_indices[:current_chain_indices.index(current_index)]:
            amicable_array[i] = -1

    elif amicable_array[current_index] > 0:
        amicable_array[starting_index] = -1

print(amicable_array.index(max(amicable_array)))

# KINDA SLOW, SORRY
