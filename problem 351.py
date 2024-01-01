import timeit


def H(limit):
    limit += 1
    orchard = [i + 1 for i in range(limit)]  # index = row, value = number of visible fruit, orchard = one segment

    for row in range(1, limit):
        for next_row in range(2 * row, limit, row):
            orchard[next_row] -= orchard[row]

    total_points = limit * (limit + 1) // 2
    seen_points = sum(orchard)
    leftmost_unseen_points = limit - 2

    return (total_points - seen_points - leftmost_unseen_points) * 6


print(H(100000000))
# takes like seven minutes
