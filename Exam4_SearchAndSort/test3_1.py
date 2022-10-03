count = 0
def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def bubble_sort(lst, right, step=1):
    for i in range(right):
        if is_sorted(lst[i:right+1]):
            right = i
            break
    for i in range(0, right):
        global count
        count += 1
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    if not is_sorted(lst):
        return bubble_sort(lst, right - 1, step + 1)

if __name__ == '__main__':
    print(" *** Bubble sort ***")    
    input_string = input("Enter some numbers : ")
    A=[]
    for n in input_string.split():
        A.append(int(n))
    bubble_sort(A,len(A))
    print()
    print(A)
    print("Data comparison =", count)