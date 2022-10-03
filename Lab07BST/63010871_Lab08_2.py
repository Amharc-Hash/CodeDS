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
            current =  self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def Below(self, node, data):
        if node == None:
            return ''
        
        ans = self.Below(node.left, data)
        if int(node.data) < int(data):
            ans = ans + str(node.data) + ' '
        ans += self.Below(node.right, data)

        return ans


if __name__ == '__main__':
    T = BST()
    inp, k = input('Enter Input : ').split('|')
    inp = [int(i) for i in inp.split()]
    for i in inp:
        root = T.insert(i)
    T.printTree(root)
    temp = T.Below(root,k)
    print('--------------------------------------------------')
    print('Below',k,':',temp if temp != '' else 'Not have')