# task_2 - transform CamelCase values to snake_case

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for name in camel_case_list:
    new_item = ''
    for index, letter in enumerate(name):
        if letter.isupper() and index != 0:
            new_item += '_' + letter.lower()
        else:
            new_item += letter.lower()
    snake_case_list.append(new_item)
print(snake_case_list)
