def firstGreaterValue(lst,key):
    lst = sorted(lst)
    for i in lst:
        if i>key:
            return i
    return "No First Greater Value"


if __name__ == '__main__':
    inp1,inp2 = input('Enter Input : ').split('/')
    lst1 = [int(e) for e in inp1.split()]
    key_lst = [int(e) for e in inp2.split()]
    for key in key_lst:
        print(firstGreaterValue(lst1.copy(), key))
