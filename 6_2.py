# task_2 - Square perimeter, area and diagonal

def square(a):
    perimeter = 4 * a
    area = a * a
    diagonal = pow(2, 0.5) * a
    return perimeter, area, diagonal


try:
    side = float(input('Please, square side value: '))
except ValueError:
    print('Only digits allowed')
else:
    if side <= 0:
        print('Only digits above zero allowed')
    else:
        print_result = square(side)
        print(f'Perimeter is: {print_result[0]}\nArea is: {print_result[1]}\nDiagonal is: {print_result[2]:.2f}')







