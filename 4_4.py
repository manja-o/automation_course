# task_4 - using continue to show names from list

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for item in names:
    if type(item) != str:
        continue
    print(item)

