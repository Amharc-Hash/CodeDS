class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class singlyLinkedlist:
    def __init__(self):
        self.head = Node(None,None)

    def __str__(self) -> str:
        sout = ''
        pos = self.head.next
        while pos is not None:
            sout += str(pos.data) + ' '
            if pos.next is not None:
                sout += '-> '
            pos = pos.next
        return sout

    def display(self):
        sout = ''
        pos = self.head.next
        while pos is not None:
            sout += str(pos.data) + ' '
            pos = pos.next
        return sout

    def size(self):
        count = 0
        pos = self.head.next
        while pos is not None:
            count += 1
            pos = pos.next
        return count

    def checkMinAndInsert(self, newValue):
        pos = self.head.next
        for index in range(self.size()):
            if newValue < pos.data:
                self.insert(index, newValue)
                return
            pos = pos.next
        else:
            self.append(newValue)

    def is_empty(self):
        return self.size() == 0

    def nodeAt(self, index):
        pos = self.head
        for _ in range(-1, index):
            pos = pos.next
        return pos

    def insert(self, index, data):
        prev_node = self.nodeAt(index-1)
        newNode = Node(data, prev_node.next)
        prev_node.next = newNode

    def append(self, data):
        self.insert(self.size(), data)

    def pop(self, index):
        if self.is_empty():
            return "Cant pop BC index is empty"
        if index > self.size()-1:
            return "Out of range"

        prev_node = self.nodeAt(index-1)
        next_node = prev_node.next.next
        popNode = prev_node.next
        prev_node.next = next_node
        return popNode

def radixSort(linkedList):
    state = False
    time = 0
    size = linkedList.size()
    zeroLinked = singlyLinkedlist()     
    oneLinked = singlyLinkedlist()      
    twoLinked = singlyLinkedlist()
    threeLinked = singlyLinkedlist()
    fourLinked = singlyLinkedlist()
    fiveLinked = singlyLinkedlist()
    sixLinked = singlyLinkedlist()
    sevenLinked = singlyLinkedlist()
    eightLinked = singlyLinkedlist()
    nineLinked = singlyLinkedlist()

    for digit in range(1000):
        for _ in range(size):
            popNode = linkedList.pop(0)

            originalData = popNode.data
            if originalData >= 0:
                calculatedData = originalData // 10 ** digit
            else:
                calculatedData = -originalData // 10 ** digit

            if calculatedData % 10 == 0:
                zeroLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 1:
                oneLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 2:
                twoLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 3:
                threeLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 4:
                fourLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 5:
                fiveLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 6:
                sixLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 7:
                sevenLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 8:
                eightLinked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 9:
                nineLinked.checkMinAndInsert(originalData)

        print('------------------------------------------------------------')
        print('Round :', digit + 1)
        print('0 :', zeroLinked.display())
        print('1 :', oneLinked.display())
        print('2 :', twoLinked.display())
        print('3 :', threeLinked.display())
        print('4 :', fourLinked.display())
        print('5 :', fiveLinked.display())
        print('6 :', sixLinked.display())
        print('7 :', sevenLinked.display())
        print('8 :', eightLinked.display())
        print('9 :', nineLinked.display())

        if not zeroLinked.is_empty() and oneLinked.is_empty() and twoLinked.is_empty() and \
                threeLinked.is_empty() and fourLinked.is_empty() and fiveLinked.is_empty() and \
                sixLinked.is_empty() and sevenLinked.is_empty() and eightLinked.is_empty() and nineLinked.is_empty():
            state = True

        while not zeroLinked.is_empty(): linkedList.append(zeroLinked.pop(0).data)
        while not oneLinked.is_empty(): linkedList.append(oneLinked.pop(0).data)
        while not twoLinked.is_empty(): linkedList.append(twoLinked.pop(0).data)
        while not threeLinked.is_empty(): linkedList.append(threeLinked.pop(0).data)
        while not fourLinked.is_empty(): linkedList.append(fourLinked.pop(0).data)
        while not fiveLinked.is_empty(): linkedList.append(fiveLinked.pop(0).data)
        while not sixLinked.is_empty(): linkedList.append(sixLinked.pop(0).data)
        while not sevenLinked.is_empty(): linkedList.append(sevenLinked.pop(0).data)
        while not eightLinked.is_empty(): linkedList.append(eightLinked.pop(0).data)
        while not nineLinked.is_empty(): linkedList.append(nineLinked.pop(0).data)

        if state is True:
            break
        time += 1
    return linkedList, time
        


# 64 8 216 512 27 729 0 1 343 125

inp = [int(i) for i in input('Enter Input : ').split()]

L = singlyLinkedlist()
L_Origin = singlyLinkedlist()

for i in inp:
    L.append(i)
    L_Origin.append(i)

time = 0
radixLinked, time = radixSort(L)
print('------------------------------------------------------------')
print(time, 'Time(s)')
print('Before Radix Sort :', L_Origin)
print('After  Radix Sort :', radixLinked)