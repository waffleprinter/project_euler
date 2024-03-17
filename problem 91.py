from math import sqrt


def is_right_angle_triangle(x0, y0, x1, y1, x2, y2):
    a_sqr = (y1 - y0) ** 2 + (x1 - x0) ** 2
    b_sqr = (y2 - y0) ** 2 + (x2 - x0) ** 2
    c_sqr = (y2 - y1) ** 2 + (x2 - x1) ** 2

    return (a_sqr + b_sqr == c_sqr or 
            a_sqr + c_sqr == b_sqr or 
            b_sqr + c_sqr == a_sqr)


grid_size = 50
answer = 0

for x1 in range(grid_size + 1):
    for y1 in range(grid_size + 1):
        if x1 == 0 and y1 == 0:
            continue

        for x2 in range(grid_size + 1):
            for y2 in range(grid_size + 1):
                if x2 == 0 and y2 == 0:
                    continue

                if x1 == x2 and y1 == y2:
                    continue

                answer += is_right_angle_triangle(0, 0, x1, y1, x2, y2)

print(answer / 2)

