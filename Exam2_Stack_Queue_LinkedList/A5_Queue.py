class Queue:
    def __init__(self):
        self.List = []

    def enQ(self,x):
        self.List.append(x)
    
    def deQ(self):
        return self.List.pop(0)
    
    def rear(self):
        return self.List[-1]
    
    def front(self):
        return self.List[0]

    def isEmpty(self):
        return self.List == []
    
    def size(self):
        return len(self.List)
    
    def isDuplicate(self):
        if len(self.List) != len(list(dict.fromkeys(self.List))):
            return "Duplicate"
        else: return "NO Duplicate"
    
Q = Queue()
es = []
left,right  = input("Enter Input : ").split("/")
left = list(left.split())
right = list(right.split(","))
for i in left:
    Q.enQ(i)
for i in range(len(right)):
    s = right[i].split()
    if s[0] == 'E':
        Q.enQ(s[1])
    elif s[0] == 'D':
        if not Q.isEmpty() :
            Q.deQ()
print(Q.isDuplicate())