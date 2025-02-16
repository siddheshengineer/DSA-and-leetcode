class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        size = 2*n-1
        result = [0]*size  # Length of the required sequence
        used = [False] * (n + 1)  # Track numbers used

        def backtrack(index: int) -> bool:
            while index < size and result[index] !=0: # Skip filled positions
                index += 1

            if index == size:  # If the sequence is filled, return True
                return True

            for num in range(n, 0, -1):  # Try numbers from largest(n is already placed) to smallest
                if used[num]: #if num is already used
                    continue

                if num == 1: # 1 only needs to be placed once
                    result[index] = 1
                    used[1] = True
                    if backtrack(index+1):
                        return True
                    result[index] = 0 #if placing 1 leads to a dead string, backtrack
                    used[1] = False
 
                else:
                    # check if both positions (index and index + num) are available
                    # if yes, place num at both positions
                    if index + num < size and result[index + num] == 0:
                        result[index] = result[index + num] = num
                        used[num] = True

                        if backtrack(index+1):
                            return True

                        result[index] = result[index + num] = 0 #if placing num leads to a dead string, backtrack
                        used[num] = False
                        
            return False  # If no number fits, return False
        
        backtrack(0) # start recusrion
        return result
        

##################faster solution####################################
# class Solution:
#     def constructDistancedSequence(self, n: int) -> List[int]:
#         res = [0] * (2 * n - 1)
#         seen = set()
#         def backtrack(i):
#             if i == len(res):
#                 return True
#             if res[i]:
#                 return backtrack(i+1)
#             for j in range(n,0,-1):
#                 if j in seen:
#                     continue
#                 seen.add(j)
#                 res[i] = j
#                 if j == 1:
#                     if backtrack(i+1):
#                         return True
#                 elif j + i < len(res) and res[i+j] == 0:
#                     res[i+j] = j
#                     if backtrack(i+1):
#                         return True
#                     res[i+j] = 0
#                 res[i] = 0
#                 seen.remove(j)
#             return False
#         backtrack(0)
#         return res

# 1718. Construct the Lexicographically Largest Valid Sequence
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer n, find a sequence that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

# Example 1:

# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
# Example 2:

# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
 

# Constraints:

# 1 <= n <= 20