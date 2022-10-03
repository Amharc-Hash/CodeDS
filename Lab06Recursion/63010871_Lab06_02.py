def palindrome(text):
    if len(text) == 1:
        return
    elif len(text) == 2 and text[0] == text[-1]:    
        return
    elif text[0] == text[-1]:
        return palindrome(text[1:-1])   #string copy start add 1 until negative index -1
    else:
        return False

inp = input('Enter Input : ')
value = palindrome(inp)

if value is False:
    print(f'\'{inp}\' is not palindrome')
else:
    print(f'\'{inp}\' is palindrome')


### comment
'''
    index in str have two meaning

    example 
    'HELLO'  len(str) = 5

    1. positive index (left to right)
        H E L L O
        0 1 2 3 4

    2. negative index (right to left)
         H  E  L  L  O
        -5 -4 -3 -2 -1

'''