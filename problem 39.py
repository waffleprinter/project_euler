"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import hypot

max_solutions = 0
max_p = 0

for p in range(1, 1001):
    current_solutions = 0

    for a in range(1, p // 2):
        for b in range(a, p // 2):
            current_p = a + b + hypot(a, b)

            if current_p > p:
                break

            if current_p == p:
                current_solutions += 1

    if current_solutions > max_solutions:
        max_solutions = current_solutions
        max_p = p

print(f"Max solutions: {max_solutions}"
      f"\nAssociated p: {max_p}")
