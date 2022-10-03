comparison = 0
def merge_Sort(lst):
    global comparison
    if len(lst) > 1:
        middle = len(lst)//2
        left = lst[:middle]
        right = lst[middle:]
        merge_Sort(left)
        merge_Sort(right)
        before, after, nextN = 0, 0, 0
        while before < len(left) and after < len(right):
            if left[before] < right[after]:
                lst[nextN] = left[before]
                before += 1
            else:
                lst[nextN] = right[after]
                after += 1
            nextN += 1
            comparison += 1
        while before < len(left):
            lst[nextN] = left[before]
            before += 1
            nextN += 1
        while after < len(right):
            lst[nextN] = right[after]
            after += 1
            nextN += 1

    

print(' *** Merge sort ***')
inp_lst = [int(i) for i in input('Enter some numbers : ').split(' ')]
merge_Sort(inp_lst)
print("\nSorted -> ",end='')
for i in range(len(inp_lst)):
        print(inp_lst[i], end=" ")
print('\nData comparison = ', comparison)