def findMax(arr):
    if len(arr) == 1: return arr[0]
    n = findMax(arr[1:])
    if n>arr[0]: return n
    else: return arr[0]

inp = [int(i) for i in input('Enter Input : ').split()]
print(f'Max : {findMax(inp)}')