"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and
down, is indicated in bold red and is equal to 2427.

131 673 234 103 018
201 096 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 037 331

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click
and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

with open("problem81matrix", "r") as f:
    matrix = [i.replace("\n", "").split(",") for i in f.readlines()]
    matrix = list(list(map(int, i)) for i in matrix)

matrix_width_max_index = len(matrix[0]) - 1  # 10
matrix_height_max_index = len(matrix) - 1  # 10

for y_pos in range(matrix_height_max_index, -1, -1):
    for x_pos in range(matrix_width_max_index, -1, -1):
        if x_pos == matrix_width_max_index and y_pos == matrix_height_max_index:
            continue

        elif y_pos == matrix_height_max_index:
            matrix[y_pos][x_pos] += matrix[y_pos][x_pos + 1]

        elif x_pos == matrix_width_max_index:
            matrix[y_pos][x_pos] += matrix[y_pos + 1][x_pos]

        else:
            right_neighbour_value = matrix[y_pos][x_pos + 1]
            bottom_neighbour_value = matrix[y_pos + 1][x_pos]

            matrix[y_pos][x_pos] += min(right_neighbour_value, bottom_neighbour_value)

print(matrix[0][0])
