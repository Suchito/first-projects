def email_slicer():
    print('Welcome to the Email Slicer ')
    print('')
    emai_input = input('Input Your email address: ')
    (username, domain) = emai_input.split('@')
    (domain, extension) = domain.split('.')
    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

while True:
    email_slicer()