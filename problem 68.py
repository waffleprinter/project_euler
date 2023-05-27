"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this
example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2;
6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the
maximum 16-digit string for a "magic" 5-gon ring?
"""

from itertools import permutations


def is_valid_gong(i):
    if i[0] + i[1] + i[2] == i[3] + i[2] + i[4] == i[5] + i[4] + i[6] == i[7] + i[6] + i[8] == i[9] + i[8] + i[1]:
        return True


largest = 0

for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    if is_valid_gong(perm):
        perm = list(map(str, perm))
        concatenated_perm = (perm[0] + perm[1] + perm[2] + perm[3] + perm[2] + perm[4] + perm[5] +
                             perm[4] + perm[6] + perm[7] + perm[6] + perm[8] + perm[9] + perm[8] + perm[1])

        if len(concatenated_perm) == 16:
            if int(concatenated_perm) > largest:
                largest = int(concatenated_perm)

        print(perm, concatenated_perm, len(concatenated_perm))

print(largest)
