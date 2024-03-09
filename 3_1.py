# task_1 - check if palindrome

original_word = input('Please, enter your word: ')
if original_word.strip().lower() == original_word.strip().lower()[::-1]:
    print('Yes, this word is palindrome')
else:
    print('No, this word is not palindrome')

