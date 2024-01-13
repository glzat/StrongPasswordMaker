import random
import time

import pyperclip


def maker(mode):
    password_length = random.randint(8, 17)
    global password
    password = ''
    if mode == 1:
        for i in range(password_length):
            kind = 1
            password += makes[kind][random.randint(0, len(makes[kind]) - 1)]
    elif mode == 2:
        for i in range(password_length):
            kind = random.randint(1, 2)
            password += makes[kind][random.randint(0, len(makes[kind]) - 1)]
    elif mode == 3:
        for i in range(password_length):
            kind = random.randint(1, 3)
            password += makes[kind][random.randint(0, len(makes[kind]) - 1)]
    return password


makes = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z'],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', ',', '.', '<', '>', '?', '/', '|', '[', ']', '{',
     '}', ':', ';', '`', '~']
]
mode = int(input("What should be included in the password?\n"
                 "1.Letters only\n"
                 "2.Letters and numbers\n"
                 "3.Letters,numbers and special symbols\n"))

ans = ''
print("Here is your password:")
while ans != 'y':
    password = maker(mode)
    ans = input(password + "\nIs this password good?(y/n):")
pyperclip.copy(password)
print("\nYour password was copied.This program will be closed in 3 seconds.")
time.sleep(3)
