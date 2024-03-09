# task_4 - last three elements of the list

text = input('Please, enter text using spaces: ')
formed_list = text.split()
if len(formed_list) >= 3:
    print(formed_list[-3::])  # or  print(formed_list[-3],formed_list[-2],formed_list[-1])
else:
    print(f'There is only {len(formed_list)} elements in list')


