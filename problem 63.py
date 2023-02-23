"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
"""
count = 1

for power in range(1, 100):
    for root in range(2, 10):
        if len(str(square := root ** power)) == power:
            count += 1
            print(root, power, square)

print(count)
"""

count = 0

for root in range(1, 10):
    exponent = 1
    power = root ** exponent

    while len(str(power)) == exponent:
        count += 1
        exponent += 1
        power = root ** exponent

print(count)
