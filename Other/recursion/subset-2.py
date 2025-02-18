class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        sequence = set()
        used = [False]*len(nums)
        nums.sort()

        def backtrack(nums, current, used, sequence, index) -> bool:

            for i in range(index, len(nums)):
                if used[i]:
                    continue
                
                if i > index and nums[i] == nums[i - 1]:  # Skip duplicates
                    continue

                current.append(nums[i])
                used[i] = True

                if tuple(current) not in sequence:
                    result.append(current[:])
                    sequence.add(tuple(current))

                    backtrack(nums, current, used, sequence, i+1)
                    
                current.pop()
                used[i] = False                

            return False
        
        backtrack(nums, [], used, sequence, 0)
        result = [[]] + result
        return result

# 90. Subsets II
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10