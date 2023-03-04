"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 =
2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three
million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""


def get_larger(first_pair, second_pair):
    n1 = first_pair[0]
    e1 = first_pair[1]

    n2 = second_pair[0]
    e2 = second_pair[1]

    if e1 > e2:
        return 1 if n1 > n2 ** (e2 / e1) else 2

    else:
        return 2 if n2 > n1 ** (e1 / e2) else 1


numbers = []

with open("problem99pairs", "r") as f:
    for pair in f.readlines():
        pair = tuple(map(int, pair.replace(",", " ").split()))
        numbers.append(pair)


largest_pair = 0

for i in range(len(numbers)):
    if get_larger(numbers[i], numbers[largest_pair]) == 1:
        largest_pair = i

print(largest_pair + 1)  # index == line - 1
