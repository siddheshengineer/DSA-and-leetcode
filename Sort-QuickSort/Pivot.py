# Helper function for QuickSort, items that are less than the pivot value on one side, and all the 
# ones that are greater on the other side.  Then we'll swap these. 
# pivot is going to do two things.
# It's going to get the list to this point where it looks like this.
# But it's also going to return the index of that for value.

def pivot(list):
    pivot_index = 0
    swap_index = pivot_index
    i = pivot_index + 1

    for _ in range(len(list)):
        if list[pivot_index] < list[i]:
            swap_index += 1
            list[swap_index], list[i] = list[i], list[swap_index]
