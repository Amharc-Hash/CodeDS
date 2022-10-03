def RotationLeft(sl):
    newstr = sl[-1]
    newstr +=sl[:-1]
    return newstr

def RotationRight(sr):
    newstr = sr[1:]+sr[0]
    return newstr

print("*** String Rotation ***")
l,r = input("Enter 2 strings : ").split()
RoLeft = l
RoRight = r
i=1
while True:
    RoLeft = RotationLeft(RoLeft)
    RoRight = RotationRight(RoRight)
    if RoLeft == l  and RoRight == r:
        #if i > 6
        #if i > 5
        if i > 5 and i!=6:
            print(" . . . . .")
        print(i,RoLeft,RoRight)
        break
    if i<=5:
        print(i,RoLeft,RoRight)
    i+=1
    if RoLeft == l and RoRight == r:
        break
print("Total of ",i,"rounds.")