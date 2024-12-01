def has_unique_chars(my_string):
    my_set = set()
    my_set.update(my_string)
    
    if len(my_string) == len(my_set):
        return True
    else:
        return False




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""