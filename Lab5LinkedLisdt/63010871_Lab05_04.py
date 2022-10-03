class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SinglyLinkedListDummy:
    def __init__(self):
        self.head = Node(None,None)
        self.cursor = Node('|',None)
        self.head.next = self.cursor

    def __str__(self) -> str:
        s_out = ''
        pos = self.head.next
        while pos is not None:
            s_out += str(pos.data) + ' '
            pos = pos.next
        return s_out

    def size(self):
        count = 0
        pos = self.head
        while pos is not None:
            count += 1
            pos = pos.next
        return count

    def prev2Cursor(self):
        pos = self.head
        if pos.next == self.cursor:
            return None
        while pos.next.next != self.cursor:
            pos = pos.next
        return pos

    def prevCursor(self):
        pos = self.head
        while pos.next != self.cursor:
            pos = pos.next
        return pos

    def aftercursor(self):
        return self.cursor.next

    def after2cursor(self):
        if self.cursor.next is None or self.cursor.next.next is None:
            return None
        return self.cursor.next.next

    def insertBeforeCursor(self,data):
        newNode = Node(data, self.cursor)
        self.prevCursor().next = newNode

    def insertAfterCursor(self, data):
        newNode = Node(data, self.cursor.next)
        self.cursor.next = newNode

    def append(self, data):
        self.insertBeforeCursor(data)

    def pop_left(self):
        prevNode = self.prev2Cursor()
        if prevNode is None:
            popNode = None
            self.head.next = self.cursor
        else:
            popNode = prevNode.next
            prevNode.next = self.cursor
        return popNode

    def pop_right(self):
        if self.cursor.next is None:
            popNode = None
        else:
            popNode = self.cursor.next
            self.cursor.next = self.after2cursor()
        return popNode
    
    def shiftCursorLeft(self):
        popNode = self.pop_left()
        if popNode is not None:
            self.insertAfterCursor(popNode.data)

    def shiftCursorRight(self):
        popNode = self.pop_right()
        if popNode is not None:
            self.insertBeforeCursor(popNode.data)



inp = input('Enter Input : ').split(',')
L = SinglyLinkedListDummy()

for i in inp:
    i = i.split()
    if i[0] == 'I':
        L.append(i[1])
    elif i[0] == 'L':
        L.shiftCursorLeft()
    elif i[0] == 'R':
        L.shiftCursorRight()
    elif i[0] == 'B':
        L.pop_left()
    elif i[0] == 'D':
        L.pop_right()

print(L)



    