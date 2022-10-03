
class Rational:
    def __init__(self,n=None,m=None):
        if n == m == None:
            self.num1 = 1
            self.num2 = 1
        else:
            self.num1 = n
            self.num2 = m

    def __lt__(self,other):
        if self.num1/self.num2 < other.num1/other.num2:return 'TRUE'
        else: return 'FALSE'
    def __gt__(self,other):
        if self.num1/self.num2 > other.num1/other.num2:return 'TRUE'
        else: return 'FALSE'
    def __ge__(self,other):
        if self.num1/self.num2 <= other.num1/other.num2:return 'TRUE'
        else: return 'FALSE'
    def __ge__(self,other):
        if self.num1/self.num2 >= other.num1/other.num2:return 'TRUE'
        else: return 'FALSE'
    def __eq__(self,other):
        if self.num1/self.num2 == other.num1/other.num2:return 'TRUE'
        else: return 'FALSE'
    def __ne__(self,other):
        if self.num1/self.num2 != other.num1/other.num2:return 'TRUE'
        else: return 'FALSE'

    def __add__(self,other):
        a1 = self.num1*other.num2
        a2 = self.num2*other.num1
        v1 = a1+a2
        v2 = self.num2*other.num2
        return str(v1)+'/'+str(v2)
    def __sub__(self,other):
        a1 = self.num1*other.num2
        a2 = self.num2*other.num1
        v1 = a1-a2
        v2 = self.num2*other.num2
        return str(v1)+'/'+str(v2)
    def __mul__(self,other):
        return str(self.num1*other.num1)+'/'+str(self.num2*other.num2)
    def __truediv__(self,other):
        return str(self.num1*other.num2)+'/'+str(self.num2*other.num1)
    def __floordiv__(self,other):
        out = self.num1*other.num2 // self.num2*other.num1
        return out

    def __str__(self):
        return ' '+str(self.num1)+'/'+str(self.num2)+' \t'


print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")
                        
str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1,d1)     # A = n1/d1
B = Rational(n2,d2)     # B = n2/d2
C = Rational()          # C = 1/1      
print("A =",A,"B =",B,'C =',C)        # method __str__
print("A < B ==> ",A<B)     # method __lt__
print("A > B ==> ",A>B)     # method __gt__
print("A <= B ==> ",A<=B)   # method __ge__
print("A >= B ==> ",A>=B)   # method __ge__
print("A == B ==> ",A==B)   # method __eq__
print("A != B ==> ",A!=B)   # method __ne__
print("A + B ==> ",A+B)     # method __add__
print("A - B ==> ",A-B)     # method __sub__
print("A * B ==> ",A*B)     # method __mul__
print("A / B ==> ",A/B)     # method __truediv__
print("A // B ==> ",A//B)     # method __floordiv__
print("A + C ==> ",A+C)  