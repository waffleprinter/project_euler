"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By
travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on
the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always
have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a
maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M
for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""

from math import gcd, ceil


def get_integer_path_cuboids(limit):
    count = 0

    for n in range(1, limit):
        for m in range(n + 1, limit + 1, 2):
            if gcd(m, n) != 1:
                continue

            leg1 = m ** 2 - n ** 2
            leg2 = 2 * m * n

            a = min(leg1, leg2)
            b = max(leg1, leg2)

            for k in range(1, limit // a + 1):
                if k * a + 1 >= ceil(k * b / 2):
                    count += k * a - ceil(k * b / 2) + 1

                if k * b <= limit:
                    count += k * a // 2

    return count


for i in range(1800, 1820):
    if get_integer_path_cuboids(i) > 1000000:
        print(i)
        break

    print(i)

# I GOT THE LIMITS FOR I BY TRIAL AND ERROR, I COULD MAKE AN ACTUAL PROGRAM TO FIND IT, BUT THIS WORKS SO EH
# THIS COULD BE WAY FASTER IF IT WAS DONE INCREMENTALLY, CURRENTLY, IT CHECKS EVERY SINGLE POSSIBILITY FOR 1800
# AND THEN EVERY SINGLE POSSIBILITY FOR 1801, AND THEN EVERY SINGLE POSSIBILITY FOR 1802 ...
