"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is
formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""

#  DO THIS BETTER, THIS IS A SUPER WEIRD SOLUTION
#  ALSO, I DIDN'T EVEN TRY TO DEAL WITH THE EDGE CASES


def get_average_point(coords):
    return (coords[0] + coords[2] + coords[4]) / 3, (coords[1] + coords[3] + coords[5]) / 3


def get_fx(coords1, coords2, x):
    x1, y1, x2, y2 = coords1[0], coords1[1], coords2[0], coords2[1]

    try:
        a = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        print(coords1, coords2)
        return 0

    b = y1 - a * x1

    return a * x + b


def origin_is_in_triangle(coords):
    A = (coords[0], coords[1])
    B = (coords[2], coords[3])
    C = (coords[4], coords[5])

    M = get_average_point(coords)

    for pair in ((A, B), (A, C), (B, C)):
        if (M[1] > get_fx(pair[0], pair[1], M[0])) != (0 > get_fx(pair[0], pair[1], 0)):
            return False

    return True


with open("problem102coordinates", "r") as f:
    coordinates = [i.replace("\n", "").split(",") for i in f.readlines()]
    coordinates = [[int(i) for i in sublist] for sublist in coordinates]

count = 0

for coords in coordinates:
    if origin_is_in_triangle(coords):
        count += 1

print(count)


