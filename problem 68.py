from itertools import permutations

solutions = []

for perm in permutations([i for i in range(1, 11)]):
    if not perm[0] == min(perm[0], perm[3], perm[5], perm[7], perm[9]):
        continue # invalid rotation

    if perm[0] + perm[1] + perm[2] == perm[3] + perm[2] + perm[4] == perm[5] + perm[4] + perm[6] == perm[7] + perm[6] + perm[8] == perm[9] + perm[8] + perm[1]:
        solutions.append(perm)

max_16_digit_solution_set = 0

for solution in solutions:
    solution_set = (
        solution[0], solution[1], solution[2], 
        solution[3], solution[2], solution[4],
        solution[5], solution[4], solution[6],
        solution[7], solution[6], solution[8],
        solution[9], solution[8], solution[1])

    concatenated_solution_set = int("".join((map(str, solution_set))))

    if concatenated_solution_set > max_16_digit_solution_set and len(str(concatenated_solution_set)) == 16:
        max_16_digit_solution_set = concatenated_solution_set

print(max_16_digit_solution_set)
