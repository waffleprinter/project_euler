"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def is_permutation_of(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def has_same_length_permutation(n, target):
    if target == 1:
        return True

    n2 = n + 1

    while len(str(n ** 3)) == len(str(n2 ** 3)):
        if is_permutation_of(n ** 3, n2 ** 3):
            return has_same_length_permutation(n2, target - 1)

        n2 += 1

    return False


for i in range(1, 1000000000):
    if has_same_length_permutation(i, 5):
        print(i ** 3)
        break


"""
cubes = {}

for i in range(1, 10000):
    key = ''.join(sorted(str(i ** 3)))

    if key not in cubes:
        cubes[key] = []

    cubes[key].append(i ** 3)

print(min([min(c) for c in cubes.values() if len(c) == 5]))
"""