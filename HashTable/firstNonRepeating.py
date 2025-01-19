def first_non_repeating_char(string):
    dict = {}
    
    for i in string:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
            
    for i in string:
        if dict[i] == 1:
            return i
    return None
        



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""