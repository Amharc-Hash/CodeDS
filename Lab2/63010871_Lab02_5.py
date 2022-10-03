def bon(w):
    if w[0] == w[1]: return (ord(w[0])-96)*4
    else: return bon(w[1:])

secretCode = input("Enter secret code : ")
print(bon(secretCode))