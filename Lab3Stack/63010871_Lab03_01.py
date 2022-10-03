class Stack:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        return self.items.append(i)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if self.isEmpty():
            return len(self.items)
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)


print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(), "Data in stack : ", s.items)
while not s.isEmpty():
    s.pop()
print(s.size(), "Data in stack : ", s.items)
