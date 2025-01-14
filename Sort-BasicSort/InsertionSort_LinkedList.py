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

    def insertion_sort(self):
        
        if self.length < 2:
            return
        
        #sorted_list = self.head
        current = self.head.next #start with 2nd element of LinkedList
        self.head.next = None #creating new sorted list, disconnecting unsorted list
        
        while current is not None:  #outer loop, previous used current.next but that caused last element to be skipped failing test cases.
            temp = current.next
            
            #to handel smallest element edge case
            if current.value <= self.head.value:
                current.next = self.head
                self.head = current
                
            #for rest of the list    
            else:
                # Traverse the sorted list to find the correct position
                sorted_list = self.head
                
                # Traverse the sorted list to find the correct position for the current node.
                # Continue moving through the sorted list as long as there is a next node
                # and the value of the next node is less than the current node's value.
                while sorted_list.next and sorted_list.next.value < current.value: 
                    sorted_list = sorted_list.next
            
                # Insert current between sorted_list and sorted_list.next
                current.next = sorted_list.next
                sorted_list.next = current
                
            current = temp #move ahead in the original list
            
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

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

