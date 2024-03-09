# task_2 - find word in text

text = input('Please, enter your text: ')
word = input('Please, enter word which you would like to find in text: ')
if text.lower().find(word.lower().strip()) != -1:
    print('Yes, this wod is present in text')
else:
    print('No, there is no such word')
