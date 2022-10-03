
def bi_search(l, r, arr, x):
    if l<= r:
        middle = (l+r)//2
        if arr[middle] == x: return True
        elif arr[middle] < x: return bi_search(middle+1,r,arr,x)
        elif arr[middle] > x: return bi_search(l,middle-1,arr,x)
    return False


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
# print(sorted(arr))
print(bi_search(0, len(arr) - 1, sorted(arr), k))
