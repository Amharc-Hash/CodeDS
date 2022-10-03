class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for item in lst:
                self.push_back(item)

    def is_empty(self):
        return self.head is None or self.tail is None

    def size(self):
        buffer = self.head
        count = 0
        while buffer is not None:
            count += 1
            buffer = buffer.next_node
        return count

    def __len__(self):
        return self.size()

    def push_front(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            buffer = Node(value, self.head)
            self.head.prev_node = buffer
            self.head = buffer

    def push_back(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            new_node = Node(value, prev_node=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def is_in(self, value):
        if self.is_empty():
            return False
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return True
            buffer = buffer.next_node
        return False

    def index(self, value):
        buffer = self.head
        count = 0
        while buffer is not None:
            if buffer.value == value:
                return count
            count += 1
            buffer = buffer.next_node
        return -1

    def pop_back(self):
        if self.is_empty():
            print('List is empty')
            return -1
        last = self.tail
        self.tail = last.prev_node
        if self.tail is not None:
            self.tail.next_node = None
        last.prev_node = None
        if self.tail is None:
            self.head = None
        return last.value

    def pop_front(self):
        if self.is_empty():
            print('List is empty')
            return -1
        first = self.head
        self.head = self.head.next_node
        if self.head is not None:
            self.head.prev_node = None
        first.next_node = None
        return first.value

    def traverse(self, rev=False):
        if self.is_empty():
            out = 'Empty'
            return out
        if rev:
            buffer = self.tail
            out = ''
            while buffer is not None:
                out += str(buffer.value)
                if buffer.prev_node is not None:
                    out += '->'
                buffer = buffer.prev_node
        else:
            buffer = self.head
            out = ''
            while buffer is not None:
                out += str(buffer.value) + ' '
                buffer = buffer.next_node
        return out

    def remove(self, value):
        if self.is_empty() or not self.is_in(value):
            print("Not Found!")
            return -1
        else:
            buffer = self.head
            while buffer is not None:
                if buffer.value == value:
                    break
                buffer = buffer.next_node
            if buffer is self.head:
                return self.pop_front()
            elif buffer is self.tail:
                return self.pop_back()
            else:
                prev_node = buffer.prev_node
                next_node = buffer.next_node
                val = buffer.value
                buffer.prev_node = None
                buffer.next_node = None
                if prev_node is not None:
                    prev_node.next_node = next_node
                if next_node is not None:
                    next_node.prev_node = prev_node
                return val

    def pop(self, pos):
        if self.is_empty() or not (0 <= pos <= self.size()-1):
            return 'Out of Range'
        else:
            if pos == 0:
                self.pop_front()
            elif pos == self.size()-1:
                self.pop_back()
            else:
                buffer = self.head
                count = 0
                while buffer is not None and count != pos:
                    count += 1
                    buffer = buffer.next_node
                prev_node = buffer.prev_node
                next_node = buffer.next_node
                buffer.prev_node = None
                buffer.next_node = None
                if prev_node is not None:
                    prev_node.next_node = next_node
                if next_node is not None:
                    next_node.prev_node = prev_node
            return 'Success'

    def insert(self, index, value):
        if index == 0 or self.is_empty():
            self.push_front(value)
        elif index >= self.size():
            self.push_back(value)
        elif index < 0:
            index = abs(index)
            count = 0
            buffer = self.tail
            while buffer is not None and count < index:
                buffer = buffer.prev_node
                count += 1
            if buffer is None:
                self.push_front(value)
            else:
                next_node = buffer.next_node
                new_node = Node(value, next_node, buffer)
                buffer.next_node = new_node
                next_node.prev_node = new_node
        else:
            count = 0
            buffer = self.head
            while buffer is not None and count != index:
                buffer = buffer.next_node
                count += 1
            prev = buffer.prev_node
            new_node = Node(value, buffer, prev)
            prev.next_node = new_node
            buffer.prev_node = new_node

    def merge(self, l1, l2):
        buffer1 = l1.head
        buffer2 = l2.tail
        out = ''
        while buffer1 is not None:
            out += str(buffer1.value) + ' '
            buffer1 = buffer1.next_node
        while buffer2 is not None:
            out += str(buffer2.value) + ' '
            buffer2 = buffer2.prev_node
        return out

    def __str__(self):
        if self.is_empty():
            return 'Empty'
        else:
            buffer = self.head
            out = ''
            while buffer is not None:
                out += str(buffer.value)
                if buffer.next_node is not None:
                    out += ' '
                buffer = buffer.next_node
            return out


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    inp = input('Enter Input (L1,L2) : ').split(' ')
    list1 = inp[0].split('->')
    list2 = inp[1].split('->')
    for j in list1:
        l1.push_back(j)
    for k in list2:
        l2.push_back(k)
    
    print(f'L1    : {l1}')
    print(f'L2    : {l2}')
    print(f'Merge : {l3.merge(l1,l2)}')

    
    
