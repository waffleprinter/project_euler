"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though
the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular
number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""


def get_decimal_value(numeral):
    numeral = numeral.replace("IV", "IIII").replace("IX", "VIIII")
    numeral = numeral.replace("XL", "XXXX").replace("XC", "LXXXX")
    numeral = numeral.replace("CD", "CCCC").replace("CM", "DCCCC")

    return sum(character_to_value_dict[char] for char in numeral)


def get_optimal_numeral(value):
    numeral = ""

    if value >= 1000:
        numeral += "M" * (value // 1000)
        value %= 1000

    if value >= 900:
        numeral += "CM"
        value %= 900

    if value >= 500:
        numeral += "D"
        value %= 500

    if value >= 400:
        numeral += "CD"
        value %= 400

    if value >= 100:
        numeral += "C" * (value // 100)
        value %= 100

    if value >= 90:
        numeral += "XC"
        value %= 90

    if value >= 50:
        numeral += "L"
        value %= 50

    if value >= 40:
        numeral += "XL"
        value %= 40

    if value >= 10:
        numeral += "X" * (value // 10)
        value %= 10

    if value >= 9:
        numeral += "IX"
        value %= 9

    if value >= 5:
        numeral += "V"
        value %= 5

    if value >= 4:
        numeral += "IV"
        value %= 4

    if value >= 0:
        numeral += "I" * (value // 1)
        value %= 1

    return numeral


with open("problem89numerals", "r") as f:
    inefficient_numerals = [i.replace("\n", "") for i in f.readlines()]

character_to_value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

numeral_values = list(map(get_decimal_value, inefficient_numerals))
efficient_numerals = list(map(get_optimal_numeral, numeral_values))

print(sum(list(map(len, inefficient_numerals))) - sum(list(map(len, efficient_numerals))))

# BETTER SOLUTION WOULD BE TO SIMPLY REPLACE ALL INEFFICIENT CHARACTERS IN INEFFICIENT_NUMERALS
# SIMPLY REPLACE "IIII" WITH "IV" FOR EXAMPLE
# THIS IS MY FIRST EVER 20% CODE THOUGH, SO I'LL KEEP IT AS A SOUVENIR I GUESS :D
