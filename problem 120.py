from math import ceil

print(sum(2 * a * ceil(a / 2 - 1) for a in range(3, 1001)))