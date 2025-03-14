class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # Quick check for already zeroed array
        if all(x == 0 for x in nums):
            return True

        coverage = [0] * (len(nums) + 1)  # Calculate coverage using difference array technique

        for l, r in queries:
            coverage[l] += 1
            coverage[r + 1] -= 1 
        
        for i in range(1, len(nums)): # Calculate prefix sum to get actual coverage
            coverage[i] += coverage[i - 1]

        for i in range(len(nums)):
            if coverage[i] < nums[i]:
                return False
        
        return True


# Why decrement at r+1 instead of r?
# The difference array technique works by marking the "start" and "end" effects of a range. When we want to apply an effect to a range [l, r]:

# We increment at position l to indicate "start applying the effect here"
# We decrement at position r+1 to indicate "stop applying the effect here"

# This works because when we calculate the prefix sum later, the effect will be applied to all positions from l up to r, but not to position r+1 and beyond.
# If we decremented at position r instead, we would incorrectly remove the effect from position r itself, which should still be covered by the query.

# 3355. Zero Array Transformation I
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

# For each queries[i]:

# Select a subset of indices within the range [li, ri] in nums.
# Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.

# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

 

# Example 1:

# Input: nums = [1,0,1], queries = [[0,2]]

# Output: true

# Explanation:

# For i = 0:
# Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
# The array will become [0, 0, 0], which is a Zero Array.
# Example 2:

# Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]

# Output: false

# Explanation:

# For i = 0:
# Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
# The array will become [4, 2, 1, 0].
# For i = 1:
# Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
# The array will become [3, 1, 0, 0], which is not a Zero Array.
 
            

                




        