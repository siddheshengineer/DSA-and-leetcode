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

    #contains using recursion
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        elif current_node.value < value:
            return self.__r_contains(current_node.right, value)
        else:
            return self.__r_contains(current_node.left, value)

    #insert using recursion
    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None: #empty tree/node
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left , value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right , value)
        return current_node

    #delete using recursion
    def _delete(self, value):
        return self._r__delete(self.root, value)
    
    def _r__delete(self, current_node, value):
        if current_node == None:
            return None
        if current_node.value > value:
            current_node.left = self._r__delete(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__delete(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                current_node.value = self.min_value(current_node.right)
                current_node.right = self._r__delete(current_node.right, current_node.value)
        return current_node
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

mytree = BSTOperations()
mytree.insert(2)
mytree.insert(1)
mytree.r_insert(3)

print("root: ", mytree.root.value)
print("root.left: ", mytree.root.left.value)
print("root.right: ", mytree.root.right.value)
# print(mytree.contains(1))
# print(mytree.r_contains(9))

mytree._delete(2)
print("root: ", mytree.root.value)
print("root.left: ", mytree.root.left.value)
print("root.right: ", mytree.root.right.value)
                
            
            
