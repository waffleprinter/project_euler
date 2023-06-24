from math import isqrt


def has_z_value(y_list):
    if len(y_list) == 1:
        return False

    for i in range(len(y_list) - 1):
        for j in range(i + 1, len(y_list)):
            if y_list[i] + y_list[j] not in square_set:
                return False

            if abs(y_list[i] - y_list[j]) not in square_set:
                return False

    return True


square_list = [i ** 2 for i in range(1, 1001)]
square_set = set(square_list)

dictionary = {}

for a in range(len(square_list) - 1):
    for b in range(a + 2, len(square_list) - 1, 2):
        x = (square_list[b] + square_list[a]) // 2
        y = (square_list[b] - square_list[a]) // 2

        if x not in dictionary:
            dictionary[x] = [y]
        else:
            dictionary[x].append(y)

for x, y in dictionary.items():
    if has_z_value(y):
        print(x, y)
        print(x + sum(y))
        break
