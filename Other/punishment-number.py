class Solution:
    def punishmentNumber(self, n: int) -> int:

        def canPartition(sqr: str, target: int, index: int, curr_sum: int) -> bool: 
            # Recursive function to check if we can partition the squared number
            if index == len(sqr):  # If we reached the end
                return curr_sum == target  # Check if sum matches target

            for i in range(index, len(sqr)):  # Try different partitions
                part = int(sqr[index:i+1])  # Extract substring as number
            
                if canPartition(sqr, target, i+1, curr_sum + part):  # Recur with updated sum
                    return True
            
            return False


        result = 0
        i = 1
        while i <= n:
            sqr = str(i*i)
            if canPartition(sqr, i, 0, 0):
                result += i*i
            i += 1
        
        return result
# Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them 
# if they lead to a dead end. The backtracking algorithm is a recursive algorithm that is used to solve problems by making a series of choices, and if
# a choice leads to a dead end, it backtracks to the last valid choice made and tries a different path. It is often used to solve problems such as 
# the N-Queens puzzle, Sudoku, and the Knight's Tour.

# 2698. Find the Punishment Number of an Integer
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a positive integer n, return the punishment number of n.

# The punishment number of n is defined as the sum of the squares of all integers i such that:

# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
 

# Example 1:

# Input: n = 10
# Output: 182
# Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
# - 1 since 1 * 1 = 1
# - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
# - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
# Hence, the punishment number of 10 is 1 + 81 + 100 = 182
# Example 2:

# Input: n = 37
# Output: 1478
# Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
# - 1 since 1 * 1 = 1. 
# - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
# - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
# - 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
# Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
 

# Constraints:

# 1 <= n <= 1000