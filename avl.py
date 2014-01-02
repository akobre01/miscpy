class AVLNode:

    def __init__(self, v):
        self.val = v
        self.right = None
        self.left = None
        self.parent = None
        self.ht = 0

    def contains(self, v):
        if self.val == v:
            return True
        elif self.left is not None and v < self.val:
            return self.left.contains(v)
        elif self.right is not None:
            return self.right.contains(v)
        else:
            return False

    def height(self, h = 1):
        if self.left is not None and self.right is not None:
            return max(self.left.height(h+1), self.right.height(h+1))
        elif self.left is not None:
            return self.left.height(h+1)
        elif self.right is not None:
            return self.right.height(h+1)
        else:
            return h

    def balanceFactor(self):
        leftHeight = 0
        rightHeight = 0
        if self.left is not None:
            leftHeight = self.left.height()
        if self.right is not None:
            rightHeight = self.right.height()
        return leftHeight - rightHeight

    def insert(self, node):
        if self.val >= node.val:
            if self.left is not None:
                self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        else:
            if self.right is not None:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self

    def insertAndBalance(self, node):
        self.insert(node)
        return node.balance()

    def rotateLeft(self):
        leftChild = self.right.left           # store my right child's left child
        oldRoot   = self.parent               # store the old root

        self.right.parent = oldRoot           # my right child's parent is my parent
        self.parent       = self.right        # my parent is now my right child
        self.right.left   = self              # my right child has me as it's left child
        self.right        = leftChild         # my new right child is the stored left child

        self.parent.attachToUnknownParent()

        return self.parent

    def rotateRight(self):
        rightChild = self.left.right          # store my left child's right child
        oldRoot    = self.parent              # store the old root

        self.left.parent = oldRoot            # my left child's parent is my parent
        self.parent      = self.left          # my parent is now my left child
        self.left.right  = self               # my left child has me as it's right child
        self.left        = rightChild         # my new left child is the stored right child

        self.parent.attachToUnknownParent()

        return self.parent

    def attachToUnknownParent(self):
        if self.parent is not None:
            if self.val > self.parent.val:
                self.parent.right = self
            else:
                self.parent.left = self

    def balance(self):
        newRoot = self
        if self.balanceFactor() > 1:
            newRoot = self.rotateRight()

        if self.balanceFactor() < -1:
            newRoot = self.rotateLeft()

        if newRoot.parent is not None:
            return newRoot.parent.balance()
        else:
            return newRoot

    def nextSmallest(self):
        if self.right is not None:
            curr = self.right
            while(curr.left is not None):
                curr = curr.left
            return curr
        else:
            return self

    def nextLargest(self):
        if self.left is not None:
            curr = self.left
            while(curr.right is not None):
                curr = curr.right
            return curr
        else:
            return self

    def inOrder(self):
        if self.left is not None:
            self.left.inOrder()
        print(self.val)
        if self.right is not None:
            self.right.inOrder()


print("Creating root at 4...")
newRoot = AVLNode(4)
print("Inserting 2...")
newRoot = newRoot.insertAndBalance(AVLNode(2))
print("Inserting 1...")
newRoot = newRoot.insertAndBalance(AVLNode(1))
print("Inserting 3...")
newRoot = newRoot.insertAndBalance(AVLNode(3))
print("Inserting 2.5...")
newRoot = newRoot.insertAndBalance(AVLNode(2.5))
print("Inserting 5...")
newRoot = newRoot.insertAndBalance(AVLNode(5))
print("Inserting 6...")
newRoot = newRoot.insertAndBalance(AVLNode(6))

print("Root of tree: " + str(newRoot.val))
print
newRoot.inOrder()
