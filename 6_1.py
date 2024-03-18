# task_1 - Sum of all numbers in range start, end

def sum_range(first, second):
    if first > second:
        temp = second
        second = first
        first = temp
    result = 0
    for i in range(first, second + 1):
        result += i
    return result


try:
    a = int(input('Please, enter start number: '))
    b = int(input('Please, enter end number: '))
except ValueError:
    print('Only digits allowed')
else:
    print('Sum is: ', sum_range(a, b))