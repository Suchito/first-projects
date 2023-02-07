def biography_info():
    try:
        name = input('Enter your name: ')
        birthday = input('Enter your date of birth: ')
        address = input('Enter your address: ')
        pg = input('What are your personal goals? ')
        print(f'Name: {name} \nDate of birth: {birthday} \nAddress: {address} \nPersonal goals: {pg}')
    except ValueError:
        print('Invalid input.')



biography_info()