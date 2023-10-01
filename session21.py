# import turtle

# main_screen = turtle.Screen()

# myturtle = turtle.Turtle()
# myturtle.color('red')
# myturtle.pensize(4)

# for i in range(4):

#     myturtle.forward(100)
#     myturtle.left(360/4)

# turtle.done()

# x = 1
# y = 1.5

# message = "hello every body"
# for c in message:
#     print(c)

# for i in range(len(message)):
#     print(message[i])

# i = 0
# while i < len(message):
#     print(message[i])
#     i += 1

import random
import string
UPPER_LETTERS = string.ascii_uppercase
LOWER_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL = '~!@#$%^&*()_+'
ALL_CHARS = UPPER_LETTERS + LOWER_LETTERS + NUMBERS + SPECIAL
def generate_password(length):
    if length < 12:
        length = 12

    password = []
    password.append(UPPER_LETTERS[random.randint(0,25)])
    password.append(LOWER_LETTERS[random.randint(0,25)])
    password.append(NUMBERS[random.randint(0,9)])
    password.append(SPECIAL[random.randint(0,12)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0,74)])

    random.shuffle(password)
    res = ""
    for p in password:
        res += p
    return res
print(generate_password(15))