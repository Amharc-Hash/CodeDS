count = 0
def sorting(lst):
    global count
    for i in range(len(lst)-1):
        count+=1
        if lst[i] > lst[i+1]:
            return False    
    return True
            

def bubble_sort(lst):
    global count
    if not sorting(lst):
        for i in range(len(lst)-1):
            # count+=1
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]
                # count+=1
        bubble_sort(lst)
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