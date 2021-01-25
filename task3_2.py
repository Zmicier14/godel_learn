import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def generate_password(dictionary):
    return_passwd = []
    count_letter = 0
    count_spec_mark = 0
    count_punc_mark = 0
    passwd = '' 
    i = 0
    while i < 20:
        rand_number = random.randrange(3)
        if rand_number == 0:
            passwd = passwd + random.choice(dictionary[0])
            count_letter += 1
        elif rand_number == 1:
            passwd = passwd + random.choice(dictionary[1])
            count_spec_mark += 1
        elif rand_number == 2:
            passwd = passwd + random.choice(dictionary[2])
            count_punc_mark += 1
        i += 1
    return_passwd = [passwd, count_letter, count_spec_mark, count_punc_mark]        
    return return_passwd

def correct_password():
    passwd = generate_password(dictionary)
    check = False
    while check != False:
        if passwd[2] > 2 and passwd[3] > 2:
            check = True
    return passwd 

dictionary = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "@#$%^&*()-_+=></", "!?.,'"]

password = correct_password()
print(f"Password is: ",end='')
print(Fore.RED+Back.WHITE+password[0])
print(f"The number of letters = {password[1]}\nThe number of special marks = {password[2]}\nThe number of punctiotional marks = {password[3]}")