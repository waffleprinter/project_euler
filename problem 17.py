"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three  hundred and  forty-two) contains 23 letters and 115 (one
 hundred and  fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

limit = 1000
english_words = []

one_to_nine = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

ten_to_nineteen = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                   16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

twenty_to_ninety = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
                    9: "ninety"}


for i in range(1, limit + 1):
    if i in one_to_nine:                     # 1 - 9
        english_words.append(one_to_nine[i])

    elif i in ten_to_nineteen:               # 10 - 19
        english_words.append(ten_to_nineteen[i])

    elif len(str(i)) == 2:                   # 20 - 99
        if int(str(i)[-1]) == 0:
            english_words.append(twenty_to_ninety[int(str(i)[0])])
        else:
            english_words.append(twenty_to_ninety[int(str(i)[0])] + one_to_nine[int(str(i)[1])])

    elif len(str(i)) == 3:                   # 100 - 999
        if int(str(i)[1:3]) == 0:
            english_words.append(one_to_nine[int(str(i)[0])] + "hundred")

        elif int(str(i)[1]) == 0:
            english_words.append(one_to_nine[int(str(i)[0])] + "hundredand" + one_to_nine[int(str(i)[2])])

        elif int(str(i)[1:3]) in ten_to_nineteen:
            english_words.append(one_to_nine[int(str(i)[0])] + "hundredand" + ten_to_nineteen[int(str(i)[1:3])])

        else:
            if int(str(i)[2]) == 0:
                english_words.append(one_to_nine[int(str(i)[0])] + "hundredand" + twenty_to_ninety[int(str(i)[1])])

            else:
                english_words.append(one_to_nine[int(str(i)[0])] + "hundredand" + twenty_to_ninety[int(str(i)[1])]
                                     + one_to_nine[int(str(i)[2])])

    else:
        english_words.append("onethousand")

print(sum(len(word) for word in english_words))
