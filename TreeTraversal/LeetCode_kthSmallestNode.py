class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    ##uisng recursion
    def kth_smallest(self, kth_index):
        self.counter = 0
        self.result = None
        
        def travers(current_node):
            
            #stop recussion if The node is None. or We’ve already found the k-th smallest element (self.result is not None).
            if not current_node or self.result is not None:
                return 
            
            #travers left
            travers(current_node.left)
            
            #current node
            self.counter += 1
            if self.counter == kth_index:
                self.result = current_node.value
                return
            
            #travers right
            travers(current_node.right)
        
        travers(self.root)
        return self.result
            


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """