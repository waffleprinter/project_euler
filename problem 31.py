"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def get_ways(target, coins):
    if len(coins) == 1:
        return target % coins[0] and 0 or 1

    return sum(get_ways(new_total, coins[1:]) for new_total in range(target, -1, -coins[0]))


print(get_ways(200, [200, 100, 50, 20, 10, 5, 2, 1]))
