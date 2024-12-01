class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTOperations:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
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
    
    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif temp.value < value:
                temp = temp.right
            else:
                temp = temp.left
        return False

        

mytree = BSTOperations()
mytree.insert(2)
mytree.insert(1)
mytree.insert(3)

print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)
print(mytree.contains(1))
                
            
            
