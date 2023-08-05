def is_valid(n):
    str_n = str(n)

    for i in range(10):
        if str_n[2 * i] != DIGIT_PLACES[i]:
            return False

    return True


num = 1010101030
DIGIT_PLACES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while not is_valid(num ** 2):
    if str(num)[-2] == "3":
        num += 40

    else:
        num += 60

print(num, num ** 2)
