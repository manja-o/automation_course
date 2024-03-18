# task_2 - Square root of number (except)

try:
    number = float(input('Please, enter your number: '))
    if number < 0:
        raise Exception("Sorry, no numbers below zero allowed")
except ValueError:
    print("Please, enter only numbers here")
else:
    sqrt = pow(number, 0.5)
    print(f'Square root of your number is {sqrt:.2f}')
finally:
    print('Calculation is finished')