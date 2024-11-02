class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):

        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev

        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return True
    
    def get(self, index):
        if( index >= 0 and index+1 <= self.length):
            if index < self.length/2:
                temp = self.head
                for _ in range (index):
                    temp = temp.next
            else:
                temp = self.tail                
                for _ in range (self.length - 1, index, -1):
                    temp = temp.prev

            return temp
        
        else:
            print('Index out of bound.')
            return None
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        temp = self.get(index)
        if temp:
            prev = temp.prev
            prev.next = new_node
            new_node.next = temp
            new_node.prev = prev
            temp.prev = new_node
            self.length += 1
            return temp
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            if temp: 
                prev = temp.prev
                after = temp.next
                prev.next = temp.next
                after.prev = temp.prev
                temp.next = None
                temp.prev = None
        self.length -= 1
        return temp
    
myclass = DoublyLinkedList(2)
myclass.append(3)
myclass.append(4)
# myclass.print_list()
# print('\n')
# myclass.pop()
# myclass.print_list()
# print(myclass.pop())
myclass.prepend(1)
myclass.prepend(0)
# myclass.print_list()
# myclass.pop_first()
myclass.print_list()
# myclass.insert(1,8)
myclass.remove(1)
myclass.print_list()