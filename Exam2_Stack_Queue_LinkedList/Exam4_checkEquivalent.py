class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def contentEquivalence(self,other):
        if len(self) != len(other):
             return False
        s1 = set()
        s2 = set()
        for i in range(len(self)): 
            s1.add(self.nodeAt(i).data)
            s2.add(other.nodeAt(i).data)
        return s1==s2

if __name__ == '__main__':
    
    inp1,inp2 = input('List1,List2 : ').split(',')
    list1 = LinkedList()
    list2 = LinkedList()
    for data in inp1.split(): list1.append(data)
    for data in inp2.split(): list2.append(data)
    print('List1 content Equivalence List2 : '+str(list1.contentEquivalence(list2)))
    