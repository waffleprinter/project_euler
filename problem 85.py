"""
Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

(check website for image)

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with
the nearest solution.
"""


def get_total_rectangles(x, y):
    return x * y * (x + 1) * (y + 1) // 4


smallest_difference = 100000000
the_area = 0

for x in range(1, 2000):
    for y in range(x, 2000):
        difference = abs(2000000 - get_total_rectangles(x, y))

        if difference < smallest_difference:
            smallest_difference = difference
            the_area = x * y

print(smallest_difference)
print(the_area)