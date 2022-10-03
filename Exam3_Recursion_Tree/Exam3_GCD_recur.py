def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

a,b = [int(i) for i in input("Enter Input : ").split()]
if a<0 and b<0:
    if a>b:a,b = b,a
elif b>a: a,b = b,a
if abs(a+b)>0: print("The gcd of {} and {} is : {}".format(a,b,abs(gcd(b,a))))
else: print("Error! must be not all zero.")