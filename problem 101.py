import sympy as sp


def a(n):
    # RETURNS 1 - N + N**2 - ... + N**8 - N**9 + N**10
    return sum(((-1) ** k) * (n ** k) for k in range(11))


def get_OP_coefficients(k):
    matrix = []

    for n in range(1, k + 1):
        row = [n ** e for e in range(k - 1, -1, -1)]
        row.append(sequence[n - 1])
        matrix.append(row)

    matrix = sp.Matrix(matrix)
    matrix_rref = matrix.rref()[0]

    return [i for i in matrix_rref.col(-1)]


def get_FIT(k):
    ans = 0

    for idx, coefficient in enumerate(get_OP_coefficients(k)):
        ans += coefficient * (k + 1) ** (k - idx - 1)

    return ans


sequence = [a(n) for n in range(1, 11)]

print(sum(get_FIT(k) for k in range(1, 11)))