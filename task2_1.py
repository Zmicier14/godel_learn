try:
    a = int(input('Please, input number: '))
    if a % 4 == 0:
        print(f'The number: {a} is a multiple of 4!')
    elif a % 2 == 0:
        print(f'{a} is even number!')
    else:
        print(f'{a} is odd number!')    
except ValueError:
    print('This is non-int format!')