class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueOperations:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:

            self.first = None
            self.last = None
            self.length -= 1
          
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
            
    

my_queue = QueueOperations(4)
my_queue.enqueue(5)
my_queue.print_queue()
print(my_queue.dequeue())
#my_queue.print_queue()