class HashTableOperations:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 47) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for pair in self.data_map[i]: 
                    all_keys.append(pair[0])
        return all_keys

"""
Big O of hash tables O(1) for all operations
"""


my_hash_table = HashTableOperations()

my_hash_table.set_item('bottle', 150)
my_hash_table.set_item('pan', 87)
my_hash_table.set_item('toffee', 108)
my_hash_table.set_item('frooti', 90)
# my_hash_table.print_table()
# print()
# print(my_hash_table.get_item('toffee'))
# print(my_hash_table.get_item('pan'))

print(my_hash_table.keys())

