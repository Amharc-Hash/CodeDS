ls = []
_check = False
max = [0,0,0]

def check_is_in(val):
    for i in range(len(ls)):
        if val == ls[i][0]:
            return i
    return -1
    
inp = list(map(int, input("Enter number end with (-1) : ").split()))
for i in range(len(inp)):
    if inp[i] == -1:
        _check = True
        break
    index = check_is_in(inp[i])
    if index == -1:
        tmp = [inp[i], 1]
        ls.append(tmp)
    else:
        ls[index][1] += 1
if _check:
    for i in range(len(ls)):
        if max[1] == 0:
            max[0],max[1] = ls[i][0],ls[i][1]
        elif max[1] < ls[i][1]:
            max[0],max[1] = ls[i][0],ls[i][1]
        elif max[1] == ls[i][1]:
            max[2] += 1
    if max[2] > 0:
        print("Not found")
    else:
        print(max[0])
else:
    print("Invalid Input !!!")