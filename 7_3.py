# task_3 - returning result of entered function if exists

def print_hi():
    result = 'Hi'
    return result


def sum_of_numbers():
    result = 5 + 6
    return result


func_name = input('Please, enter function name: ')
try:
    print(eval(func_name))
except NameError:
    print('There is no such function')


