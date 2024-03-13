# task_5 - using break to stop after non int value was found

types = [1, 1000, 2, 12, {'key': 'value'}]
for item in types:
    if type(item) == int:
        print(item)
    else:
        print(f'цикл не працює з {type(item)} типом даних')
        break


