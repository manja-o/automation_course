# task_3 - Calculator with (+, -, *, /) operations

counter = 0
while counter < 2:
    first_number = float(input('Please, enter first number: '))
    second_number = float(input('Please, enter second number: '))
    operation = input('Please, choose operation that need to be done from the list: +, -, *, /: ')
    if operation == '+':
        print(f'{first_number} + {second_number} = {first_number + second_number}')
    elif operation == '-':
        print(f'{first_number} - {second_number} = {first_number - second_number}')
    elif operation == '*':
        print(f'{first_number} * {second_number} = {first_number * second_number}')
    elif operation == '/':
        if second_number == 0:
            print('Division by zero is forbidden')
            counter += 1
        else:
            print(f'{first_number} / {second_number} = {(first_number / second_number):.2f}')
    else:
        print('Incorrect operation')
        counter += 1
    if counter == 0:
        break
    if counter == 2:
        print('You have used all attempts')
