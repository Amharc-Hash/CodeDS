class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.lst = []

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
        return self.root
    
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        self.lst.append(node.data)
        self.inOrder(node.right)

    def printTree(self, node, level = 0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

def closestValue(root, value):
    X = None
    T.inOrder(root)
    for i in T.lst:
        X = i
        if i == value or i > value:
            break

    print("Closest value of {} : {}".format(value,X))
   

T = BST()
inp, num = input('Enter Input : ').split('/')
num = int(num)
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
    T.printTree(root)
    print("-"*50)
closestValue(root, num)