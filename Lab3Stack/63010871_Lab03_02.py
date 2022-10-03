class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        return self.items.append(i)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def clear(self):
        return self.items.clear()

def ManangeStack(inp):
    lst = Stack()
    temp = Stack()
    lastNum = 0
    for i in inp:
        comm = i.split()
        if comm[0] == 'A':
            print(f'Add = {comm[1]}')
            lst.push(int(comm[1]))

        if comm[0] == 'P':
            if lst.isEmpty(): print(-1)
            else:
                print(f'Pop = {lst.pop()}')
                
        if comm[0] == 'D':
            if lst.isEmpty(): print(-1)
            else:
                while not lst.isEmpty():
                    if int(lst.peek()) == int(comm[1]):
                        print(f'Delete = {lst.pop()}')
                    else: temp.push(int(lst.pop()))    
                while not temp.isEmpty(): lst.push(int(temp.pop()))   

        if comm[0] == 'LD':
            if lst.isEmpty(): print(-1)
            else:
                while not lst.isEmpty():
                    if int(lst.peek()) < int(comm[1]):
                        print(f'Delete = {int(lst.peek())} Because {int(lst.peek())} is less than {int(comm[1])}')
                        lst.pop()
                    else: temp.push(int(lst.pop()))    
                while not temp.isEmpty(): lst.push(int(temp.pop()))   
                
        if comm[0] == 'MD':
            if lst.isEmpty(): print(-1)
            else:
                while not lst.isEmpty():
                    if int(lst.peek()) > int(comm[1]): 
                        print(f'Delete = {int(lst.peek())} Because {int(lst.peek())} is more than {int(comm[1])}')
                        lst.pop()
                    else: temp.push(int(lst.pop()))    
                while not temp.isEmpty(): lst.push(int(temp.pop()))

    return lst.items   


inp = input('Enter Input : ').split(',')
k = ManangeStack(inp)
print(f'Value in Stack = {k}')


