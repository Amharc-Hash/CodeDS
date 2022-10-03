
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


def E(i):
    q.enqueue(i)
    print(f'Add {i} index is {q.size()-1}')

def D():
    if q.isEmpty(): 
        print(-1)
    else: 
        print(f'Pop {q.dequeue()} size in queue is {q.size()}')
    

q = Queue()
inp = input('Enter Input : ').split(',')
# count = 0
for i in inp:
    comm = i.split(' ')
    if comm[0] == 'E': E(comm[1])
    if comm[0] == 'D': D()
if q.isEmpty(): print('Empty')
else: print(f'Number in Queue is :  {q.items}')


        
