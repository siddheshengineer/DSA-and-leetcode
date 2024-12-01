def find_pairs(arr1, arr2, target):
    set1 = set()
    set2 = set()
    set1.update(arr1)
    set2.update(arr2)
    ans = []
    
    for i in set1:
        j = target - i
        if j in set2:
            ans.append((i,j))
    ans.sort()
    return ans



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""