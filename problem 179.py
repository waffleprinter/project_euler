limit = 10 ** 7

number_of_divisors = [2 for i in range(limit)]
number_of_divisors[0] = 0
number_of_divisors[1] = 1

for divisor in range(2, limit):
    for i in range(2 * divisor, limit, divisor):
        number_of_divisors[i] += 1

ans = 0

for i in range(limit - 1):
    if number_of_divisors[i] == number_of_divisors[i + 1]:
        ans += 1

print(ans)
