def remove_duplicates(my_list):
    my_set = set()
    ans = []
    
    my_set.update(my_list)
    for i in my_set:
        ans.append(i)
    
    return ans



my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""