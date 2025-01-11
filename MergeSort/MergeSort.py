from Merge import merge

#doesn't sort the list in place, return separate sorted list
def merge_sort(unsorted_list):

    if len(unsorted_list) == 1: #stop condition for recursion, because single element list is by definition sorted
        return unsorted_list 

    #break the list in half till it is a single element
    mid_index = int(len(unsorted_list)/2)
    left  = merge_sort(unsorted_list[:mid_index])
    right = merge_sort(unsorted_list[mid_index:])

    return merge(left, right)

print(merge_sort([3,1,4,2]))


##Big O
# Space complexity is O(n), basic sorting are O(1)
# Time complexity is O(n log n), basic sorting are O(n^2). Much better than basic sorting