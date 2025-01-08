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
        
        sorted_list = self.head
        current = sorted_list.next
        sorted_list.next = None
        
        while current.next is not None:
            temp = current.next
            
            if current.value <= self.head.value:
                current.next = self.head
                self.head = current
                
            else:
                while current.next is not None:
                    current.value 
                    
            
            
            current = temp
            
    
    # def insertion_sort(list):
    #   for i in range (1, len(list)):
    #     temp = list[i]
    #     j = i - 1

    #     while temp < list[j] and j > -1:
    #         list[j+1] = list[j]
    #         list[j] = temp
    #         j -= 1

    #   return list 





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

