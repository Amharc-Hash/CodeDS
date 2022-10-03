def find_alphabet(text):
    for character in text:
        if ord('a') <= ord(character) <= ord("z"): return character
    return None

def alphabet_sort(lst):
    prep = []
    for item in lst:
        prep.append((find_alphabet(item), item))    #append 
        # print(prep)
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-1-i):
            if prep[j][0] > prep[j+1][0]:
                prep[j], prep[j+1] = prep[j+1], prep[j]
                swapped = True
        if not swapped: break
    last_lst = []
    for items in prep:
        last_lst.append(items[1])
    return last_lst


if __name__ == '__main__':
    lst = input("Enter Input : ").split(' ')
    output = alphabet_sort(lst)
    for items in output:
        print(items, end=" ")