## need to improve

def imp_heap(arr,n,i):
    largest = i
    left = 2*i+1
    right  = 2*i+2

    if left < n and arr[largest] < arr[left]:
        largest = 1
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        imp_heap(arr,n,largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        imp_heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        imp_heap(arr,i,0)

if __name__ == '__main__':
    # arr = list(map(int,input('Enter Input : ').split()))
    arr = [3,7,4,5,2,1]
    heap_sort(arr)
    n = len(arr)
    print('sort is')
    for i in range(n):
        print(arr[i], end=' ')