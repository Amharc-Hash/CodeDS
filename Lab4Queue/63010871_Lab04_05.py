dict = {'[': '',']': '','\'': '',',': '',' ': ''}

def replace_all(string):
    for key, value in dict.items():
        string = string.replace(key, value)
    return string

class Queue:
    def __init__(self, list=None):
        if list is not None:
            self.items = list
        else:
            self.items = []
        self.explode = 0
        self.fail = 0

    def __str__(self):
        return replace_all(str(self.items))

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, new_data):
        self.items.append(new_data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return -1

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return -1

    def head(self):
        if not self.is_empty():
            return self.items[0]
        return -1

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return -1

    def reverse(self):
        if not self.is_empty():
            temp = []
            s = self.size()
            for i in range(s):
                temp.append(self.items.pop())
            self.items = temp
            return temp
        return []


token = list(input('Enter Input (Normal, Mirror) : ').split(' '))

normal = Queue()
mirror = Queue()

for i in token[0]:
    normal.enqueue(i)
for i in token[1]:
    mirror.enqueue(i)

temp = Queue()
interrupt = Queue()
count = 1
after = mirror.peek()
while(not mirror.is_empty()):

    temp.enqueue(mirror.pop())

    if count == 3:
        count = 1
        temp.pop()
        temp.pop()
        interrupt.enqueue(temp.pop())
        while(not temp.is_empty()):
            mirror.items.append(temp.pop())
        after = ''
        mirror.explode += 1
    if after == mirror.peek():
        count += 1
    else:
        count = 1
        after = mirror.peek()

temp.reverse()
mirror.items = temp.items
temp.items = []
count = 1

normal.reverse()
after = normal.peek()
while not normal.is_empty():
    temp.enqueue(normal.pop())
    if count == 3:
        count = 1
        if not interrupt.is_empty():
            after = temp.peek()
            temp.pop()
            temp.enqueue(interrupt.head())
            temp.enqueue(after)
            if interrupt.head() == temp.peek():
                temp.pop()
                temp.pop()
                temp.pop()
                normal.fail += 1
            interrupt.dequeue()
            
        else:
            temp.pop()
            temp.pop()
            temp.pop()
            normal.explode += 1
        while(not temp.is_empty()):
            normal.enqueue(temp.pop())
        after = ''

    if after == normal.peek():
        count += 1
    else:
        count = 1
        after = normal.peek()


normal.items = temp.reverse()

print('NORMAL :',normal.size(),sep='\n')
if not normal.is_empty():
    print(normal)
else:
    print('Empty')
print(normal.explode,end=' ')
print('Explosive(s) ! ! ! (NORMAL)')
if normal.fail > 0:
    print('Failed Interrupted',normal.fail,'Bomb(s)')
print('------------MIRROR------------',': RORRIM',sep='\n')
print(mirror.size())
if not mirror.is_empty():
    print(mirror)
else:
    print('ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE',mirror.explode)