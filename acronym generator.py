def acronym():
    user_input = input('Enter a full meaning of organization or concept: ')
    phrase = (user_input.replace('of', '')).split()
    acronym = ''
    for word in phrase:
        acronym = acronym + word[0].upper()
    print(f'Acronym of {user_input} is {acronym}')

acronym()
