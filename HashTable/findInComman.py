def find_in_common(list1, list2):
    dict = {}

    for i in list1:
        dict[i] = True
    
    for i in list2:
        if i in dict:
            return True
    
    return False

list1 = [2, 3, 4, 9, 5]
list2 = [1, 7, 8, 0, 5]

print(find_in_common(list1, list2))
