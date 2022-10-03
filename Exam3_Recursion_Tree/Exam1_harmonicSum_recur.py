x= ""
def harmonic_sum(n):
    output = 0
    if n==1:
        global x
        x += str(n)+" "
        return 1 
    output += 1/n + harmonic_sum(n-1)
    x += str(1)+"/"+str(n)+" "
    return output

print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
y = harmonic_sum(num)
k = x.split()
print(" + ".join(k),'= ',end="")
print("%.8f" %(y))