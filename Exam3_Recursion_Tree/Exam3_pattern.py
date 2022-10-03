#2n-1 square
def pattern(i,j):
    if i+2 == 1: return
    else:
        print('^'*int(i) + '#'*(j) + '^'*int(i))    
        return pattern(i-1,j+2)

inp = int(input('Enter Input : '))
if inp<1: print('Not Draw!')
else:
    i=inp-1
    j=1
    pattern(i,j)