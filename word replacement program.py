def replace_word():
    string='Hi guys i`m Bartek'
    word_to_replace= input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(string.replace(word_to_replace, word_replacement))

replace_word()