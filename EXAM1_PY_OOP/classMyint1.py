import re
class MyInt:
    def __init__(self,n):
        self.num = n
        self.x = []

    def isPrime(self):
        for k in range(2, self.num):
            if (self.num % k) == 0 and self.num > 1: 
                return str(self.num) + ' isPrime : False'
        return str(self.num) + ' isPrime : True'
        #return str(self.num) + ' isPrime : ' + str(not re.match(r"^1?$|^(1+?)\1+$", "1" * self.num))

    def showPrime(self):
        for i in range(2, self.num + 1):
            for j in range(2,i):
                if i%j == 0:
                    break
            else : self.x.append(str(i))
        return 'Prime number between 2 and ' + str(self.num) + ' : ' + str(' '.join(map(str,self.x)))

    def __sub__(self,another):
        return str(self.num) + " - " + str(another.num) + ' = ' + str(self.num - (another.num // 2))

n,m = list(map(int,(input("Enter 2 number : ").split())))
a = MyInt(n)
b = MyInt(m)
print(a.isPrime())
print(b.isPrime())
print(a.showPrime())
print(b.showPrime())
print(a-b)