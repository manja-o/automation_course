# task_1 - Square root of number (raise, finally)

number = float(input('Please, enter your number: '))
try:
    if number < 0:
        raise Exception("Sorry, no numbers below zero allowed")
    else:
        sqrt = pow(number, 0.5)
        print(f'Square root of your number is {sqrt:.2f}')
finally:
    print('Calculation is finished')
