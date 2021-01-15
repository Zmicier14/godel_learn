def input_number(a):
    b = None
    while b == None:        #Как-то по-другому можно сделать выход из этого цикла?
        try:
            b = float(input(f'Please input the {a} number = '))
        except ValueError:
            print('Please input right number!')
    return b

d = input_number('1st')
e = input_number('2nd')