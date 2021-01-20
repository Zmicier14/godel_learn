import random

dictionary = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "@#$%^&*()-_+=></", "!?.,'"]
#letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#special_mark = '@#$%^&*()-_+=></'
#punc_mark = '!?.,'
count_letter = 0
count_spec_mark = 0
count_punc_mark = 0
passwd = ''
i = 0
#while i < 20:
#    try:
#        char = random.choice(letters)

 
while i < 20:
    rand_number = random.randrange(3)
    if rand_number == 0:
        passwd = passwd + random.choice(dictionary[0])
    elif rand_number == 1:
        passwd = passwd + random.choice(dictionary[1])
    elif rand_number == 2:
        passwd = passwd + random.choice(dictionary[2])
    i += 1    

print(passwd)