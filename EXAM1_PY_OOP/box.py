text1 = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F',\
    'G','H','I','J','K','L','M','N','O','P','Q','R','S',\
        'T','U','V','W','X','Y','Z']

row = 0
col = 0
temp = 1
inp = int(input('Enter a positive number : '))
for i in range(inp):
    for j in range(inp):
        if(col==len(text1)) : col = 0
        if(row==len(text1)) : row = 0
        if(temp==len(text1)) : temp = 0
        if i == 0 : print(text1[col], end=' ')
        elif j == 0 and i != 0 : print(text1[row], end=' ')
        elif j == inp-1 and i != 0 : print(text1[row-1], end=' ')
        elif j != inp-1 and j != 0 and i == inp-1:
            print(text1[temp-1], end=' ')
            temp+=1
        else: print(' ', end=' ')
        col+=1

    row+=1
    print()
