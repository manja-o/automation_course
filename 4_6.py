# task_6 - same symbols count

entered_value = input('Please, enter your text: ')
dict = {}
dict_for_print = {}
for index, letter in enumerate(entered_value):
    x = entered_value.count(letter)
    dict.update({letter: x})
# formed_line = ' '.join([f'{letter},{x}' for letter, x in dict.items()])
formed_line = ' '.join([f'{letter},{dict.get(letter)}' for letter in dict])
print(formed_line)

