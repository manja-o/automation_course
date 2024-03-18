# task_3 - Calculator 3.0

counter = 1
while counter == 1:

    try:
        first_number = float(input('Please, enter first number: '))
        second_number = float(input('Please, enter second number: '))
    except ValueError:
        print('Only digits allowed')
    else:
        operation = input("Please, choose operation that need to be done: +, -, *, / or exit: ")

        try:
            if operation == '+':
                result = first_number + second_number
                print(f'{first_number} + {second_number} = {result}')
            elif operation == '-':
                result = first_number - second_number
                print(f'{first_number} - {second_number} = {result}')
            elif operation == '*':
                result = first_number * second_number
                print(f'{first_number} * {second_number} = {result}')
            elif operation == '/':
                if second_number == 0:
                    print("Division by zero is forbidden")
                else:
                    result = first_number / second_number
                    print(f'{first_number} / {second_number} = {result:.2f}')
            elif operation == 'exit':
                counter = 0
            else:
                print('Incorrect operation')
        except ValueError:
            print('Incorrect operation - entered value should be +, -, *, / or exit')
    finally:
        print('------------------')
