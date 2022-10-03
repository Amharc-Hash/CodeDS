def drome(lst):
    is_descending = True
    is_ascending = True
    is_unique = True
    is_same = True
    unique_lst = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]: is_descending = False
        if lst[i] > lst[i+1]: is_ascending = False
        if lst[i] in unique_lst: is_unique = False
        if lst[i] != lst[i+1]:
            is_same = False
        unique_lst.append(lst[i])
    if lst[len(lst)-1] in unique_lst:
        is_unique = False

    if is_same: return "Repdrome"
    elif is_ascending and is_unique: return "Metadrome"
    elif is_ascending and not is_unique: return "Plaindrome"
    elif is_descending and is_unique: return "Katadrome"
    elif is_descending and not is_unique: return "Nialpdrome"
    else: return "Nondrome"

if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ")))
    print(drome(in_lst))