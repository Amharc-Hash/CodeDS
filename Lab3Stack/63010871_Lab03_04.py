class Stack:
    def __init__(self, list = None):
        if list is None: self.items = []
        else: self.items = list
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
        return self.items[-1]

S = Stack()
countA = 0
inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    # print(f'i loop : {i}')
    if i == 0 and 'A' in inp[0]:
        temp = inp[0].split()
        S.push(int(temp[1]))
    elif 'A' in inp[i]:
        temp = inp[i].split()
        # print(f'temp : {temp}')
        # print(f'peek : {S.peek()}')
        # print(int(temp[1]))
        if S.isEmpty():
            S.push(0)
        if int(temp[1]) < S.peek():
            S.push(int(temp[1]))
            # print(f'temp < peek : {S.items}')
        elif int(temp[1]) >= S.peek():
            # print(f'temp > peek : {S.items}')
            for j in range(S.size()):
                # print(f'size in pop: {S.size()}')
                if not S.isEmpty() and int(temp[1]) >= S.peek():
                    S.pop()
                    # print(f'pop : out {S.pop()}')
                    # print(S.items)
            # print(int(temp[1]))
            S.push(int(temp[1]))
    elif 'B' in inp[i]:
        print(S.size())
        # print(f'size B : {S.size()}')
