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

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def breadth(self):
        Q = list()
        Q.append(self.root)
        while Q:
            n = Q.pop(0)
            print(n, end=" ")
            if n.left:
                Q.append(n.left)
            if n.right:
                Q.append(n.right)


T = BST()
print(" *** Binary Search Tree ***")
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print()
print(" --- Tree traversal ---")
print("Level order : ", end="")
T.breadth()
print("\nPreorder : ", end="")
T.preorder()
print("\nInorder : ", end="")
T.inorder()
print("\nPostorder : ", end="")
T.postorder()