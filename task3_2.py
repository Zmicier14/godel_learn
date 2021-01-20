import random

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

def check_password():
    passwd = generate_password(dictionary)
    check = False
    while check != False:
        if passwd[1] > 2 and passwd[2] > 2 and passwd[3] > 2:
            check = True
    return passwd[0] 

dictionary = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "@#$%^&*()-_+=></", "!?.,'"]
#temp_passwd = generate_password(dictionary))
print(check_password())