def insertion_sort(list):
    for i in range (1, len(list)):
        temp = list[i]
        j = i - 1

        while temp < list[j] and j > -1:
            list[j+1] = list[j]
            list[j] = temp
            j -= 1

    return list 

print(insertion_sort([4,2,6,1,3,5]))
print(insertion_sort([40,22,6,15,3,54]))

## Big O of insertion sort usually is O(n^2) but for a almost sorted list it can be O(n)