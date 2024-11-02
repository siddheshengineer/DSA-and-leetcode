class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):

        temp = self.head
        pre = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        elif self.length == 0:
            return None
        
        else:
            while(temp.next):
                pre = temp
                temp = temp.next 
 
            self.tail = pre
            self.tail.next = None 
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp
        
    def get(self, index):
        # print(self.length)
        if( index >= 0 and index+1 <= self.length):
            if index == 0:
                return self.head
            else:
                i = 0
                temp = self.head
                while(i != index):
                    temp = temp.next
                    i += 1
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

        #second way to do this
        # if( index < 0 or index >= self.length):
        #     return None
        # temp= self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return temp
        # return temp.value

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.head
            pre = self.head
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = new_node
            new_node.next = temp
            self.length += 1
            return True

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        else:
            temp = self.get(index-1)
            if temp:
                delete = temp.next
                temp.next = delete.next
                delete.next = None
                self.length -= 1
                return delete

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedList(1)
my_linked_list.append(4)
my_linked_list.append(5)

# my_linked_list.print_list()

# my_linked_list.pop()
# my_linked_list.print_list()

my_linked_list.prepend(0)
my_linked_list.print_list()
# print("After first pop")
# my_linked_list.pop_first()
# my_linked_list.print_list()

# print('\nBelow is value of get:')
# print(my_linked_list.get(0))

# print('New set values list is:')
# print(my_linked_list.set_value(1,6))
# print(my_linked_list.insert(1,6))

# print(my_linked_list.remove(2))
my_linked_list.reverse()
print('\nAfter reversal\n')
my_linked_list.print_list()