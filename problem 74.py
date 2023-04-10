"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out
that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""


def get_factorial_chain_length(n, previous_nums):
    digit_sum = sum(factorial_dict[i] for i in str(n))

    if digit_sum in previous_nums:
        return len(previous_nums | {n})

    return get_factorial_chain_length(digit_sum, previous_nums | {n})


factorial_dict = {"0": 1,
                  "1": 1,
                  "2": 2,
                  "3": 6,
                  "4": 24,
                  "5": 120,
                  "6": 720,
                  "7": 5040,
                  "8": 40320,
                  "9": 362880}


count = 0

for i in range(1, 1000000):
    if get_factorial_chain_length(i, set()) == 60:
        count += 1

print(count)

# TAKES AROUND 80 SECONDS
# VERY UNOPTIMIZED, I KNOW, BUT I COULDN'T BE BOTHERED TO FIX IT :d
