def mod_position(arr, s):
    temp = []
    test = [char for char in arr]
    for (i, v) in enumerate(test):
        if s == 1:
            return test
        elif (i+1) % s == 0 and i != 0 and s != 1:
            temp.append(v)
    return temp


print('*** Mod Position ***')
strIn, sub = input('Enter Input : ').split(',')
value = mod_position(strIn, int(sub))
print(value)
