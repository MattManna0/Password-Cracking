import time


potential_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                   "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                   "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g",
                   "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3",
                   "4", "5", "6", "7", "8", "9", "0", " ", "!", "?", "stopping_point"]
print(len(potential_chars))

char_length = len(potential_chars)

first_letter = None

password = "J8"
index = len(password)



# for one digit passwords
if index == 1:
    for char in potential_chars:
        first_letter = char
        if first_letter == password:
            print("Your password has been breached. It is {}"
                .format(first_letter))
            break
        else:
            continue


second_index = 0

first_index = 0


# for two digit passwords
if index == 2:
    while True:
        first_letter = potential_chars[first_index]
        second_letter = potential_chars[second_index]
        two_letter_guess = first_letter + second_letter
        if two_letter_guess == password:
            print("Your password has been breached. it is {}"
                  .format(two_letter_guess))
            break
        elif second_letter == "stopping_point":
            first_index += 1
            second_index = 0
        elif two_letter_guess != password:
            second_index += 1
        else:
            print("Error: invalid password entered")


first_index = 0

second_index = 0

third_index = 0


# for three digit passwords
if index == 3:
    while True:
        first_letter = potential_chars[first_index]
        second_letter = potential_chars[second_index]
        third_letter = potential_chars[third_index]
        three_letter_guess = first_letter + second_letter + third_letter
        if three_letter_guess == password:
            print("Your password has been breached. It is {}"
                  .format(three_letter_guess))
            break
        elif third_letter == "stopping_point":
            second_index += 1
            third_index = 0
        elif second_letter == "stopping_point":
            third_index = 0
            second_index = 0
            first_index += 1
        elif three_letter_guess != password:
            third_index += 1
        else:
            print("Error: invalid password entered")


first_index = 0

second_index = 0

third_index = 0

fourth_index = 0


# for four digit passwords
if index == 4:
    while True:
        first_letter = potential_chars[first_index]
        second_letter = potential_chars[second_index]
        third_letter = potential_chars[third_index]
        fourth_letter = potential_chars[fourth_index]
        four_letter_guess = first_letter + second_letter + third_letter + fourth_letter
        if four_letter_guess == password:
            print("Your password has been breached. It is {}"
                  .format(four_letter_guess))
            break
        elif fourth_letter == "stopping_point":
            third_index += 1
            fourth_index = 0
        elif third_letter == "stopping_point":
            second_index += 1
            third_index = 0
            fourth_index = 0
        elif second_letter == "stopping_point":
            first_index += 1
            second_index = 0
            third_index = 0
            fourth_index = 0
        elif four_letter_guess != password:
            fourth_index += 1
        else:
            print("Error: invalid password entered:")



first_index = 0

second_index = 0

third_index = 0

fourth_index = 0

fifth_index = 0


t1 = time.time()
# for 5 digit passswords
if index == 5:
    while True:
        first_letter = potential_chars[first_index]
        second_letter = potential_chars[second_index]
        third_letter = potential_chars[third_index]
        fourth_letter = potential_chars[fourth_index]
        fifth_letter = potential_chars[fifth_index]
        five_letter_password = first_letter + second_letter + third_letter + fourth_letter + fifth_letter
        if five_letter_password == password:
            print("Your password has been breached. it is {}"
                  .format(five_letter_password))
            break
        elif fifth_letter == "stopping_point":
            fifth_index = 0
            fourth_index += 1
        elif fourth_letter == "stopping_point":
            fifth_index = 0
            fourth_index = 0
            third_index += 1
        elif third_letter == "stopping_point":
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index += 1
        elif second_letter == "stopping_point":
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index = 0
            first_index += 1
        elif five_letter_password != password:
            fifth_index += 1
        else:
            print("Error: invalid password entered")
t2 = time.time()
time = (t2 - t1)
print("Your password has been breached in {} seconds"
      .format(time))



first_index = 0

second_index = 0

third_index = 0

fourth_index = 0

fifth_index = 0

sixth_index = 0



# for six digit passwords
if index == 6:
    while True:
        first_letter = potential_chars[first_index]
        second_letter = potential_chars[second_index]
        third_letter = potential_chars[third_index]
        fourth_letter = potential_chars[fourth_index]
        fifth_letter = potential_chars[fifth_index]
        sixth_letter = potential_chars[sixth_index]
        six_digit_password = first_letter + second_letter + third_letter + fourth_letter + fifth_letter + sixth_letter
        if six_digit_password == password:
            print("Your password has been breached. It is {}"
                  .format(six_digit_password))
            break
        elif sixth_letter == "stopping_point":
            sixth_index = 0
            fifth_index += 1
        elif fifth_letter == "stopping_point":
            sixth_index = 0
            fifth_index = 0
            fourth_index += 1
        elif fourth_letter == "stopping_point":
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index += 1
        elif third_letter == "stopping_point":
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index += 1
        elif second_letter == "stopping_point":
            sixth_index = 0
            fifth_index = 0
            fourth_index = 0
            third_index = 0
            second_index = 0
            first_index += 1
        elif six_digit_password != password:
            sixth_index += 1
        else:
            print("Error: invalid password entered"