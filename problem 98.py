"""
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216
= 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not
permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

# FORGIVE ME

with open("problem98words", "r") as f:
    words = f.read().replace('"', '').split(",")

anagrams = {"".join(sorted(word)): [] for word in words}

for word in words:
    anagrams["".join(sorted(word))].append(word)

anagrams = [a for a in anagrams.values() if len(a) != 1]


squares = [i ** 2 for i in range(1, 31623)]
anagramic_squares = {"".join(sorted(str(num))): [] for num in squares}

for num in squares:
    anagramic_squares["".join(sorted(str(num)))].append(num)

anagramic_squares = [a for a in anagramic_squares.values() if len(a) != 1]

mapped_anagrams = []


for anagram_group in anagrams:
    mapping = {}

    for letter in anagram_group[0]:
        if letter not in mapping:
            mapping[letter] = str(len(mapping) + 1)

    mapped_words = []

    for anagram in anagram_group:
        mapped_word = ""
        for letter in anagram:
            mapped_word += mapping[letter]
        mapped_words.append(mapped_word)

    mapped_anagrams.append(mapped_words)

print(anagrams)
print(mapped_anagrams, "\n")

mapped_squares = []

for anagram_group in anagramic_squares:
    mapping = {}

    for digit in str(anagram_group[0]):
        if digit not in mapping:
            mapping[digit] = str(len(mapping) + 1)

    mapped_words = []

    for anagram in anagram_group:
        mapped_word = ""
        for digit in str(anagram):
            mapped_word += mapping[digit]
        mapped_words.append(mapped_word)

    mapped_squares.append(mapped_words)

print(anagramic_squares[:100])
print(mapped_squares[:100], "\n")

for i in range(len(mapped_anagrams) - 1):
    anagram_group = mapped_anagrams[i]

    for j in range(len(mapped_squares) - 1):
        square_anagram_group = mapped_squares[j]

        if sorted(set(anagram_group).intersection(set(square_anagram_group))) == sorted(anagram_group):
            print(anagram_group, square_anagram_group)
            print(anagrams[i], anagramic_squares[j])
            print("")

# I'M SO SORRY
# BY THE WAY, YOU HAVE TO MANUALLY CHECK THE OUTPUTS TO GET THE ANSWER, CUZ I'M TOO LAZY TO CODE IT


