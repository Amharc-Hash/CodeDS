class MyInt:
    def __init__(self,n):
        self.number = n
        self.num = n
    def toRoman(self):
        roman = ''
        x = self.number
        Dec = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        Roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        i = len(Dec) - 1
        while self.number!=0:
            if self.number >= Dec[i]:
                roman += Roman[i]
                self.number = self.number-Dec[i]
                #i+=1
            else: i-=1
        return str(x)+" convert to Roman : "+str(roman) 
    def __add__(self,other):
        return str(self.num)+" + "+str(other.num)+" = "+str((self.num+other.num)+int((self.num+other.num)/2))
        #return str(self.num)+" + "+str(other.num)+" = "+str(int((self.num+other.num)))

print(" *** class MyInt ***")
n,m = list(map(int,(input("Enter 2 number : ").split())))
a = MyInt(n)
b = MyInt(m)
print(a.toRoman())
print(b.toRoman())
print(a+b)