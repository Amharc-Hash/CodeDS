count = 0

def bubble_sort(lst):
    global count
    n = len(lst)
    for i in range(n-1):
        # count+=1
        for j in range(n-i-1):
            count+=1
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            # count+=1
    return lst

if __name__ == '__main__':
    print(" *** Bubble sort ***")    
    input_string = input("Enter some numbers : ")
    A=[]
    for n in input_string.split():
        A.append(int(n))
    bubble_sort(A)
    print()
    print(A)
    print("Data comparison =", count)