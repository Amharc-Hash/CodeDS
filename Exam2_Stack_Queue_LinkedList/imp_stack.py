class Stack:
    def __init__(self,data=None):
        if data is not None:
            self.items = data
        else:
            self.items = []

    def size(self):
        return len(self.items)

    def pop(self):
        self.items.pop()
    
    def push(self, data):
        self.items.append(data)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []
    
    def bottom(self):
        if not self.isEmpty():
            return self.items[0]
        else: return None

    def __str__(self):
        if not self.isEmpty():
            out = 'In Stack : '
            for item in self.items:
                out += str(item)+' '
            return out
        else: return 'Empty'
inp = input()
print(inp)

    