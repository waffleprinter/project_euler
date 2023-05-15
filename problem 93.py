"""
By using each of the digits from the set, 1, 2, 3, 4, exactly once, and making use of the four arithmetic operations
(+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, 1, 2, 3, 4, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n,
can be obtained, giving your answer as a string: abcd.
"""

import timeit
from itertools import permutations, combinations, product


def get_equations(n, s):
    a, b, c, d = n[0], n[1], n[2], n[3]
    s1, s2, s3 = s[0], s[1], s[2]

    equations = [f"{a} {s1} {b} {s2} {c} {s3} {d}",
                 f"({a} {s1} {b}) {s2} {c} {s3} {d}",
                 f"{a} {s1} ({b} {s2} {c}) {s3} {d}",
                 f"{a} {s1} {b} {s2} ({c} {s3} {d})",
                 f"({a} {s1} {b}) {s2} ({c} {s3} {d})",
                 f"({a} {s1} {b} {s2} {c}) {s3} {d}",
                 f"{a} {s1} ({b} {s2} {c} {s3} {d})",
                 f"(({a} {s1} {b}) {s2} {c}) {s3} {d}",
                 f"({a} {s1} ({b} {s2} {c})) {s3} {d}",
                 f"{a} {s1} (({b} {s2} {c}) {s3} {d})",
                 f"{a} {s1} ({b} {s2} ({c} {s3} {d}))"]

    return equations


def get_consecutive_length(nums):
    largest = 1

    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            largest += 1

        else:
            break

    return largest


start = timeit.default_timer()

symbol_combinations = [symbol_combination for symbol_combination in product(["+", "-", "*", "/"], repeat=3)]
longest_chain_and_its_nums = (1, [1])

for num_combination in combinations([str(i) for i in range(1, 11)], 4):
    reachable_integers = set()

    for nums in permutations(num_combination):
        for symbols in symbol_combinations:
            for equation in get_equations(nums, symbols):
                try:
                    equation_evaluation = float(eval(equation))
                except ZeroDivisionError:
                    equation_evaluation = -1.0

                if equation_evaluation.is_integer() and equation_evaluation > 0:
                    reachable_integers.add(equation_evaluation)

    chain_length_and_nums = (get_consecutive_length(sorted(reachable_integers)), num_combination)

    if chain_length_and_nums[0] >= longest_chain_and_its_nums[0]:
        longest_chain_and_its_nums = chain_length_and_nums
        print(longest_chain_and_its_nums)


print(longest_chain_and_its_nums)

