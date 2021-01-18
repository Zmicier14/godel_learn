def input_number(a):
    user_input = None
    while user_input == None:  # Как-то по-другому можно сделать выход из этого цикла?
        try:
            user_input = float(input(f"Please input the {a} number = "))
        except ValueError:
            print("Please input right number!")
    return user_input

#Adding a commit
first_number = input_number("1st")
second_number = input_number("2nd")
while True:
    operation = input("Input the arifmethic operation(+,-,/,*):")
    if operation == "+":
        print("Result = ", first_number + second_number)
        break
    elif operation == "-":
        print("Result = ", first_number - second_number)
        break
    elif operation == "/" and second_number == 0:
        print("Division by zero!")
    elif operation == "/" and second_number != 0:
        print("Result = ", first_number / second_number)
        break
    elif operation == "*":
        print("Result = ", first_number * second_number)
        break
    else:
        print("Input correct operation!")
