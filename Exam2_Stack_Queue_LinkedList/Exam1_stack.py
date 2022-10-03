"""
จงสร้างโครงสร้างข้อมูล Stack ที่มี method ดังต่อไปนี้ 
__str__ สำหรบแสดงข้อมูลที่อยู่ใน stack
push(data) สำหรับเก็บข้อมูล data   
pop() สำหรับนำข้อมูลออก
isEmpty() สำหรับตรวจสอบว่า stack ว่างไหม ถ้าว่าง ให้เป็น True
size() สำหรับแสดงขนาดของ stack ว่ามีข้อมูลกี่ตัว
peek() สำหรับแสดงค่าข้อมูลที่อยู่ที่อยู่บนสุด
bottom() สำหรับแสดงค่าข้อมูลที่อยู่ล่างสุด
"""

class Stack:
    def __init__(self,data=None):
        if data is not None: self.items = data
        else : self.items = []

    def __str__(self):
        if not self.isEmpty():
            x = "Data in Stack is : "
            for data in self.items:
                x += str(data)+' '
            return x
        return 'Empty'

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else: return

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return

    def bottom(self):
        if not self.isEmpty():
            return self.items[0]
        return None

if __name__ == '__main__':
    inp = int(input('Enter choice : '))
    if inp == 1:
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())
    elif inp == 2:
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.isEmpty())
    elif inp == 3:
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())