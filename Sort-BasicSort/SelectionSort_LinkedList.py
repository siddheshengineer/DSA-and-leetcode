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
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def selection_sort(self):
        
        if self.length < 2:
            return
        
        unsorted_head = self.head
        
        while unsorted_head != self.tail:
            current = unsorted_head
            min_value = unsorted_head
            
            while current.next is not None:
                next_node = current.next
                if min_value.value > next_node.value:
                    min_value = next_node
                    
                current = next_node
            
            if min_value.value != unsorted_head.value:
                
                min_value.value, unsorted_head.value = unsorted_head.value, min_value.value
                
            unsorted_head = unsorted_head.next
            

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

