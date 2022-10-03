def rotationRight(x):
    temp = x[1:]+x[0]
    return temp

def rotationLeft(x):
    temp = x[-1]+x[:-1]
    return temp

print("*** String Rotation ***")
left,right = input("Enter 2 strings : ").split()
RotateLeft = left
RotateRight = right
i=1

while True:
    RotateRight = rotationRight(RotateRight)
    RotateLeft = rotationLeft(RotateLeft)
    
    if RotateLeft == left  and RotateRight == right:
        if i > 6 :
            print(" . . . . .")
        print(i,RotateLeft,RotateRight)
        break
    if i<=5:
        print(i,RotateLeft,RotateRight)
    i+=1
    if RotateLeft == left  and RotateRight == right:
        break
print(f'Total of  {i} rounds.')