def subarray_sum(nums, target):
    sums = 0
    _hash = {}
    
    for index, i in enumerate(nums):

        sums += i
        diff = sums - target
        print(f"Sum is: {sums}")
        print(f"Diff is: {diff}")
        
            
        if sums == target:
            print("Inside sums == target if")
            print(list([0, index]))
            return [0, index]

        if diff in _hash:
            print("Inside 2nd if block")
            # print(([_hash[diff]+1, index]))
            return [_hash[diff]+1, index]
        
        _hash[sums] = index
    
    return [] 
        
    
        




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
