#the is for heap starting at zero position, for heap starting at 1st, to minus 1. 
# i.e for left child it will be 2*index, parent index // 2
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self, index):
        return 2*index+1
    
    def right_child(self, index):
        return 2*index+2

    def parent(self, index):
        return (index -1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
                self.swap(current, self.parent(current))
                current = self.parent(current)
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)

        return max_value

    def sink_down(self, index):
        max_index = index
        
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if (left_index < len(self.heap)) and (self.heap[max_index] < self.heap[left_index]):
                max_index = left_index

            if (right_index < len(self.heap)) and (self.heap[max_index] < self.heap[right_index]):
                max_index = right_index
            
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return


myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)

# myheap.insert(11)
# print(myheap.heap)

# myheap.insert(5)
# print(myheap.heap)

print(myheap.remove())
print(myheap.heap)
print(myheap.remove())
print(myheap.heap)