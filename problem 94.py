"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the
almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by
no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose
perimeters do not exceed one billion (1,000,000,000).
"""

# IF YOU WANT TO WORK ON THIS, JUST MAKE IT FASTER. IT TAKES LIKE A TRILLION YEARS

from math import gcd, sqrt

limit = 1000000000
count = 0

n_limit = int((-6 + sqrt(36 - 16 * (3 - limit))) / 8)

for n in range(1, n_limit + 1):
    m_limit = int((-n + sqrt(n ** 2 + 2 * limit)) / 2)

    if 2 * (n + 1) * (2 * n + 1) > limit:
        break

    for m in range(n + 1, m_limit + 1, 2):
        if 2 * m * (m + n) > limit:
            break

        if gcd(m, n) != 1:
            continue

        m_squared = m ** 2
        n_squared = n ** 2

        leg1 = m_squared - n_squared
        leg2 = 2 * m * n

        a = min(leg1, leg2)
        b = max(leg1, leg2)
        c = m_squared + n_squared

        if 2 * a == c + 1 or 2 * a == c - 1:
            print(a, b, c)
            count += 2 * (a + c)

print(count)