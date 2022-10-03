# sum / input
# example
# 2/ -1 0 3 2
#print
# [-1,3]
# [0,2]

def bubble_sort(lst):
    result = lst.copy()
    for i in range(len(result)-1):
        swapped = False
        for j in range(len(result)-1-i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def subset_sum(target, lst, left=0, res=[], carry=[]): #BACK AND FORTH : NEED TO IMPROVE
    if left >= len(lst):                                # Can you explain to anyone?
        return res                                      # Nope? So Shut the fuck up and
    carry.append(lst[left])                             # Learn
    if sum(carry) == target:
        res.append(carry.copy())
    res = subset_sum(target, lst, left+1, res, carry)
    carry.pop()
    res = subset_sum(target, lst, left+1, res, carry)
    return res


def list_sorting(lst):                              #SORT MIN TO MAX Like bubble sort
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


if __name__ == '__main__':
    inp = input("Enter Input : ").split('/')
    goal = int(inp[0])
    original_lst = list(map(int, inp[1].split()))
    original_lst = bubble_sort(original_lst)
    viable_lst = subset_sum(goal, original_lst)
    if len(viable_lst) == 0:
        print("No Subset")
    else:
        viable_lst = list_sorting(viable_lst)
        for item in viable_lst:
            print(item)