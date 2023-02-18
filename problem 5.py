"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

answer = 2520
i = 19

while i > 10:
    if answer % i == 0:
        i -= 1

    else:
        answer += 2520
        i = 19

print(answer)
