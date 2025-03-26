class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        numbers = []

        for row in grid:
            for num in row: # Flatten the grid to 1-D list
                if num % x != grid[0][0] % x: # stop early if the  there's a diff in remainder values
                    return -1
                numbers.append(num)
                
        numbers.sort() # get medium of listed, to get min no of operations
        median = numbers[len(numbers) // 2]
        result = 0

        for nums in numbers:
            result += abs(median - nums) // x
        
        return result

# 2033. Minimum Operations to Make a Uni-Value Grid
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.