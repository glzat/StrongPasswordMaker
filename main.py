import random
import time

import pyperclip


# lower_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# upper_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# character = [',','.','!','?','_','#','^']
# number = ['0','1','2','3','4','5','6','7','8','9']

def maker(mode):
    password_length = random.randint(8, 17)
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
mode = int(input('请选择组合:\n1.只包含字母\n2.数字和字母\n3.数字、字符和字母\n'))

ans = ''
password = ''
print('您的密码是：')
while (ans != 'y'):
    password = maker(mode)
    ans = input(password + '\n是否满意？（y/n）:')
pyperclip.copy(password)
print('\n您的代码已复制到粘贴板，程序将于3秒后自动关闭')
time.sleep(3)
