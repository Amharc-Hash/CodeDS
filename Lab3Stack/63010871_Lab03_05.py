class Stack:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list
        tempo = []

    def push(self, i):
        return self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def clear(self):
        return self.items.clear()

hTree = Stack()
def B():
    count = 0
    hLast = 0
    Tempo = Stack()
    while not hTree.isEmpty():
        if int(hTree.peek())>hLast:
            hLast = int(hTree.peek())
            count += 1
        Tempo.push(hTree.pop())

    while not Tempo.isEmpty(): hTree.push(Tempo.pop())
    return count

def S():
    Tempo1 = Stack()
    while not hTree.isEmpty():
        if int(hTree.peek())%2 == 0:
            if int(hTree.peek())-1 > 0: Tempo1.push(int(hTree.pop())-1)
        else: Tempo1.push(int(hTree.pop())+2)
    while not Tempo1.isEmpty(): hTree.push(Tempo1.pop())

inp = input('Enter Input : ').split(',')
for i in inp:
    inpCommand = i.split(" ")
    if inpCommand[0] == 'A': hTree.push(inpCommand[1])
    if inpCommand[0] == 'B': print(B())
    if inpCommand[0] == 'S': S()





