# task_3 - dictionary with programming languages

dict = {'python': 'Guido van Rossum', 'c++': 'Bjarne Stroustrup', 'java': 'James Gosling', 'javascript': 'Brendan Eich'}
for key, value in dict.items():
    print(f'My favorite programming language is {key}. It was created by {value}.')
dict.pop('c++')
print('Dictionary after one pair removing:', dict)



