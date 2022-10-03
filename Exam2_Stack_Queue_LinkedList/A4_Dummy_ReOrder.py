class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.Dummyhead = Node(None)
        self.tail = self.Dummyhead
        self.size = 0 

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.Dummyhead.next, ""
        while cur is not None:
            s += str(cur.value) + " <- " if cur.next is not None else str(cur.value)
            cur = cur.next
        return s
    
    def isEmpty(self):
        return self.size == 0 
    
    def append(self, data):
        newNode = Node(data)
        if self.isEmpty(): 
            self.Dummyhead.next = newNode
            self.tail = newNode
        else:
            current = self.tail 
            current.next = newNode
            self.tail = newNode
        self.size+=1
    
    def insertBefore(self,node,data):
        newNode = Node(data)
        prev = node
        current = node.next
        prev.next,newNode.next = newNode,current
        self.size += 1
    
    def insert(self, pos, data):
        if int(pos) == 0 or self.size+int(pos) <= 0:
            self.addHead(data)
        elif int(pos) >= self.size:
            self.append(data)
        else:
            if pos < 0:
                self.insertBefore(self.nodeAt(self.size - abs(pos)-1),data)
            else:
                self.insertBefore(self.nodeAt(pos-1),data)
    
    def index(self,data) :
        current = self.Dummyhead.next
        for i in range(self.size) :
            if current.value == data:
                return i
            current = current.next
        return -1
    
    def Size(self):
        return self.size
    
    def nodeAt(self,i) :
        current = self.Dummyhead.next
        for j in range(0,i) :
            current = current.next
        return current

    def newLL(self):
        if self.Dummyhead.next != self.nodeAt(self.index("0")): 
            p = self.nodeAt(self.index("0") - 1)
            p.next,head = None,p.next
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = self.Dummyhead.next
            self.Dummyhead.next = head
        else:pass

print(" *** Re order ***")
inp = input("Enter Input : ").split()
L = LinkedList()
for x in inp:
    L.append(x)
print("Before : {}".format(L))
L.newLL()
print("After : {}".format(L))