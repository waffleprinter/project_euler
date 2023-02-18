"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import problem22numbers

names = sorted(problem22numbers.names)
total_name_score = 0

for i in range(0, len(names)):
    sum_letter_positions = 0

    for letter in names[i]:
        sum_letter_positions += ord(letter) - 64

    total_name_score += sum_letter_positions * (i + 1)

print(total_name_score)

