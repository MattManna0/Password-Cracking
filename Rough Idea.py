import time

password = input("Please enter your password to be tested: ")

t1 = time.time()

possible_chars = ["Starting_Point", "a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k",
                  "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                  "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G",
                  "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                  "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "?", "0",
                  "9", "8", "7", "6", "5", "4", "3", "2", "1",
                  "Stopping_Point"]

first_index = 0
second_index = 0
third_index = 0
fourth_index = 0
fifth_index = 0
sixth_index = 0
seventh_index = 0


if len(password) == 1:
    while first_index != 65:
        guess = possible_chars[first_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                  .format(guess))
            break
        else:
            first_index += 1

if len(password) == 2:
    while first_index != 65:
        guess = possible_chars[first_index] + possible_chars[second_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                .format(guess))
            break
        elif second_index == 65:
            second_index = 0
            first_index += 1
        else:
            second_index += 1

if len(password) == 3:
    while first_index != 65:
        guess = possible_chars[first_index] + possible_chars[second_index] + \
                possible_chars[third_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                  .format(guess))
            break
        elif third_index == 65:
            third_index = 0
            second_index += 1
        elif second_index == 65:
            third_index = 0
            second_index = 0
            first_index += 1
        else:
            third_index += 1


if len(password) == 4:
    while first_index != 65:
        guess = possible_chars[first_index] + possible_chars[second_index] + \
                possible_chars[third_index] + possible_chars[fourth_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                .format(guess))
            break
        elif fourth_index == 65:
            fourth_index = 0
            third_index += 1
        elif third_index == 65:
            fourth_index = 0
            third_index = 0
            second_index += 1
        elif second_index == 65:
            fourth_index = 0
            third_index = 0
            second_index = 0
            first_index += 1
        else:
            fourth_index += 1


if len(password) == 5:
    while first_index != 65:
        guess = possible_chars[first_index] + possible_chars[second_index] + \
                possible_chars[third_index] + possible_chars[fourth_index] + \
                possible_chars[fifth_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                  .format(guess))
            break
        elif fifth_index == 65:
            fifth_index = 0
            fourth_index += 1
        elif fourth_index == 65:
            fifth_index = 0
            fourth_index = 0
            third_index += 1
        elif third_index == 65:
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index += 1
        elif second_index == 65:
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index = 0
            first_index += 1
        else:
            fifth_index += 1


if len(password) == 6:
    while first_index != 65:
        guess = possible_chars[first_index] + possible_chars[second_index] + \
                possible_chars[third_index] + possible_chars[fourth_index] + \
                possible_chars[fifth_index] + possible_chars[sixth_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                  .format(guess))
            break
        elif sixth_index == 65:
            sixth_index += 0
            fifth_index += 1
        elif fifth_index == 65:
            sixth_index = 0
            fifth_index = 0
            fourth_index += 1
        elif fourth_index == 65:
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index += 1
        elif third_index == 65:
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index += 1
        elif second_index == 65:
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index = 0
            first_index += 1
        else:
            sixth_index += 1


if len(password) == 7:
    while first_index != 65:
        guess = possible_chars[first_index] + possible_chars[second_index] + \
                possible_chars[third_index] + possible_chars[fourth_index] + \
                possible_chars[fifth_index] + possible_chars[sixth_index] + \
            possible_chars[seventh_index]
        if guess == password:
            print("Your password has been breached. It is {}"
                .format(guess))
            break
        elif seventh_index == 65:
            seventh_index = 0
            sixth_index += 1
        elif sixth_index == 65:
            seventh_index += 0
            sixth_index += 0
            fifth_index += 1
        elif fifth_index == 65:
            seventh_index = 0
            sixth_index = 0
            fifth_index = 0
            fourth_index += 1
        elif fourth_index == 65:
            seventh_index = 0
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index += 1
        elif third_index == 65:
            seventh_index = 0
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index += 1
        elif second_index == 65:
            seventh_index = 0
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index = 0
            first_index += 1
        else:
            seventh_index += 1


t2 = time.time()
print("I took {} seconds to crack"
      .format(t2 - t1))