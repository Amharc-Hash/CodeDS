def perf(num):
    output = []
    for i in range(1,num):
        if num%i==0:
            output.append(i)
    return output

print(' *** Perfect Number Verification ***')
num = int(input('Enter number : '))
if num<0:
    print('Only positive number !!!')
else:
    lst = perf(num)
    if sum(lst) == num:
        print(f'{num} is a PERFECT NUMBER.')
    else:
        print(f'{num} is NOT a perfect number.')
print('Factors :',lst)

