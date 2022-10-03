print('Enter username')
name = str(input())
print('Enter username')
password = str(input())

if name == 'myname' and password == 'mypassword':
    print('Login successfully')
    print('Welcome to Currency Conversion App')
    print('Enter \'b2u\' to convert Bath to USD')
    print('Enter \'u2b\' to convert USD to Bath')
    sel = str(input())
    if sel == 'b2u':
        print('Enter your money(Bath)')
        bath = int(input())
        print(f'Your USD exchange is {bath/33.87}')
    elif sel == 'u2b':
        print('Enter your money(USD)')
        us = int(input())
        print(f'Your Bath exchange is {us*33.87}')
    else: print('Please enter only \'b2u\' or \'u2b\'')
else: print('login fail')