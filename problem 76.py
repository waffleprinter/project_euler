"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""


def recursive(n, k):
    if k == 1:
        return 1

    if (n, k) in recursive_dict:
        return recursive_dict[(n, k)]

    if k == 2:
        return n // 2

    total_sum = 0

    for i in range(1, n // k + 1):
        new_n = n - k * i

        for j in range(1, k):
            total_sum += recursive(new_n, j)

    recursive_dict[(n, k)] = total_sum
    return total_sum


recursive_dict = {}

target = 100
total = 0

for k_ in range(1, target - 1):
    total += recursive(target, k_)

print(total)

# CHECK OUT THE PARTITION FUNCTION GENERATING FUNCTION FOR A BETTER SOLUTION :d
