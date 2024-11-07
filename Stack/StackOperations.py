class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackOperations:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        print("\nHeight is: " + str(self.height))

    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value


mystack = StackOperations(1)
mystack.push(2)
mystack.push(0)
mystack.print_stack()
mystack.pop()
mystack.print_stack()
