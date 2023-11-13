def get_pascals_triangle(rows):
    triangle = [[0, 1, 0]]

    for row_index in range(1, rows):
        row = [0]
        previous_row = triangle[row_index - 1]

        for value_index in range(1, len(previous_row)):
            row.append(previous_row[value_index - 1] + previous_row[value_index])

        row.append(0)

        triangle.append(row)

    return triangle


def get_primes(n):
    sieve = [True] * n
    primes = [2]

    for i in range(4, n, 2):
        sieve[i] = False

    for p in range(3, n, 2):
        if sieve[p]:
            primes.append(p)

            for i in range(p ** 2, n, p):
                sieve[i] = False

    return primes


def is_square_free(n):
    for squared_prime in squared_primes:
        if n % squared_prime == 0:
            return False

        if squared_prime >= n:
            break

    return True


primes = get_primes(11243247)
squared_primes = list(map(lambda x: x ** 2, primes))

pascals_triangle = get_pascals_triangle(51)
pascals_values = set()

for row in pascals_triangle:
    for value in row[1:-1]:
        pascals_values.add(value)

square_free_values = set()

for value in pascals_values:
    if is_square_free(value):
        square_free_values.add(value)

print(sum(square_free_values))



