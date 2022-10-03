print(" *** String count ***")
inp = input("Enter message : ").split()
lower = []
upper = []
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j].islower():
            lower.append(inp[i][j])
        elif inp[i][j].isupper():
            upper.append(inp[i][j])
print("No. of Upper case characters :",len(upper)) 
print("Unique Upper case characters :","  ".join(sorted(list(set(upper))))) 
print("No. of Lower case Characters :",len(lower)) 
print("Unique Lower case characters :","  ".join(sorted(list(set(lower)))))