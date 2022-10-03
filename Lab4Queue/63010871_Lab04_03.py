class Queue:
    def __init__(self, list = None):
        if list == None: self.items = []
        else: self.items = list
    
    def enqueue(self,i):
        return self.items.append(i)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

q = Queue()
sp1 = Queue()
inp = input('Enter code,hint : ').split(',')
for i in inp[0]:
    sp1.enqueue(ord(i))
diff = int(sp1.items[0]) - ord(inp[1])
while not sp1.isEmpty():
    q.enqueue(int((sp1.dequeue()) - diff))
while not q.isEmpty():
    sp1.enqueue(chr(q.dequeue()))
    print(sp1.items)