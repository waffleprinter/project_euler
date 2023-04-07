"""
Starting in the top left Corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

[DOWN, DOWN, RIGHT, RIGHT], [DOWN, RIGHT, DOWN, RIGHT], [DOWN, RIGHT, RIGHT, DOWN]
[RIGHT, RIGHT, DOWN, DOWN], [RIGHT, DOWN, RIGHT, DOWN], [RIGHT, DOWN, DOWN, RIGHT]

How many such routes are there through a 20×20 grid?
"""


def how_many_paths(x, y):
    if x < y:
        return "Invalid, input the values so that x >= y"

    number_of_paths = x + 1
    variables = [3]
    change = 3

    for i in range(x - 2):
        variables.append(variables[-1] + change)
        change += 1

    for i in range(1, y):
        number_of_paths += variables[-1]
        variables[0] += 1

        for j in range(1, len(variables)):
            variables[j] += variables[j - 1]

    return number_of_paths


print(how_many_paths(20, 20))

