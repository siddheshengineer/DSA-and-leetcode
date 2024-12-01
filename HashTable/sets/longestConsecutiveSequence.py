def longest_consecutive_sequence(my_list):
    _set = set(my_list)
    #print(_set)
    max_lenght = 0
    for i in _set:
        if i-1 not in _set:
            count = 1
            current_num = i
            
            while current_num + 1 in _set:
                count += 1
                current_num += 1
            
            max_lenght = max(max_lenght,count)
                
    return max_lenght
    

    
    
    
    



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""