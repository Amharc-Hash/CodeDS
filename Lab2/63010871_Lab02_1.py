def Rshift(num, shift):
    tempo = []
    st = 0
    binary = bin(num).replace('0b', '')
    tempList = list(binary)
    if tempList[0] == '-':
        tempList.remove('-')
        st = 1
    if shift >= len(tempList):
        if st == 1:
            return -1
        else:
            return 0
    else:
        for i in range(shift):
            tempList.pop()

    for (i, v) in enumerate(tempList):
        numTemp = int(v)
        tempo.append(numTemp * pow(2, len(tempList) - i - 1))

    if st == 1:
        summ = -sum(tempo)
    else:
        summ = sum(tempo)
    return summ


n, s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n), int(s)))
