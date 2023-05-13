# write basic code for tree class

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def PreOrderTraversal(self):
        print(self.data)
        if self.left:
            self.left.PreOrderTraversal()
        if self.right:
            self.right.PreOrderTraversal()

    def InOrderTraversal(self):
        if self.left:
            self.left.InOrderTraversal()
        print(self.data)
        if self.right:
            self.right.InOrderTraversal()

    def PostOrderTraversal(self):
        if self.left:
            self.left.PostOrderTraversal()
        if self.right:
            self.right.PostOrderTraversal()
        print(self.data)



#wrtie a main function to test the code by adding some values and calling preorder and inorder traversal

if __name__ == "__main__":
    root = Tree(10)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(8)
    root.insert(11)
    root.insert(18)
    