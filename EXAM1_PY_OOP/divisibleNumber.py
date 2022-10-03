print(" *** Divisible number ***")
inp = int(input("Enter a positive number : "))
x = []
if inp <= 0:
    print(inp,"is OUT of range !!!")
else:
    for i in range(1,inp+1):
        if inp%i == 0:
            x.append(i)
    print("Output ==>"," ".join(list(map(str,x))))
    print("Total ==>",len(x))