list1 = list(map(int, input("Enter Your List : ").split()))
value = []
if len(list1) < 3: print('Array Input Length Must More Than 2')
else:
    for i in range(len(list1)-2):
        for j in range(i+1, len(list1) - 1):
            for k in range(j+1, len(list1)):
                temp = []
                temp.append(list1[i])
                temp.append(list1[j])
                temp.append(list1[k])
                if sum(temp) == 0 and temp not in value: value.append(temp)

    print(value)

