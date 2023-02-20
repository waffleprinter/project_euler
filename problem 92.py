"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has
been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


def ends_with_89(n):
    while n != 1 and n != 89:
        n = sum(squares[i] for i in str(n))

    return n == 89


squares = {str(i): i ** 2 for i in range(10)}
ending_in_89 = {i for i in range(1, 568) if ends_with_89(i)}
answer = 0

for i in range(1, 10000001):
    if sum(squares[j] for j in str(i)) in ending_in_89:
        answer += 1

print(answer)

