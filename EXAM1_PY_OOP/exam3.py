def check_in(value):
    for i in range(len(lst)):
        if value == lst[i][0]:
            return i
    return -1

lst = []
_status = False
check = [0,0,0]
inp = list(map(int, input('Enter number end with (-1) : ').split()))

for i in range(len(inp)):
    if inp[i] == -1:
        _status = True
        break
    index = check_in(inp[i])
    if index == -1:
        temp = [inp[i], 1]
        lst.append(temp)
    else:lst[index][1] += 1

if _status:
    for i in range(len(lst)):
        if check[1] == 0: check[0],check[1] = lst[i][0],lst[i][1]
        elif check[1] < lst[i][1]: check[0],check[1] = lst[i][0],lst[i][1]
        elif check[1] == lst[i][1]: check[2] += 1
    if check[2] > 0 and inp[0] != -1: print('Not found')
    elif inp[0] == -1: print("Not found")
    else : print(check[0])
else:
    print("Invalid INPUT !!!")