def natural_sum(n):
    if n<1:return 0
    else:
        sum = n+natural_sum(n-1)
        if n == num: print(n,end=' = ')
        else: print(n,end=' + ')
        return sum

print(' *** Natural sum ***')
num = int(input("Enter number : "))
print('%.d' %(natural_sum(num)))