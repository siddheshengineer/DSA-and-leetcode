class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        ## Line Sweep approch ##
        # Initialize
        n = len(nums)
        sums, k = 0, 0
        diff_array = [0] * (n + 1)

        # Iterate through nums. For each index
        for i in range(n):
            while (sums + diff_array[i]) < nums[i]:

                k += 1
                if k > len(queries):
                    return -1
                l, r, v = queries[k-1]

                if r >= i:
                    diff_array[max(l, i)] += v
                    diff_array[r+1] -= v
            
            sums += diff_array[i]
        
        return k




        ## Binary Search approch ##

        # def isValid(org_nums: List[int], queries: List[List[int]], k: int) -> bool:

        #     nums = org_nums.copy()

        #     coverage = [0] * (len(nums) + 1)  # Calculate coverage using difference array technique

        #     for i in range(0, k):
        #         coverage[queries[i][0]] += queries[i][2] # Update L value with Val
        #         coverage[queries[i][1] + 1] -= queries[i][2] # Update R value with Val

            
        #     prefix_sum = 0
        #     for i in range(len(nums)):
        #         prefix_sum += coverage[i]            
                
        #         if prefix_sum < nums[i]:
        #             return False
                
        #     return True
             
 

        # # Binary Search Part

        # l = 0
        # r = len(queries) # k has to be in b/w 0 and len(queries)

        # while l < r:
        #     mid = l + (r - l) // 2

        #     if isValid(nums, queries, mid):
        #         r = mid - 1
            
        #     else: 
        #         l = mid + 1

        # return l if l < len(queries) else -1  # Return -1 if no valid solution


# This is where a line sweep approach comes into play. Line sweeping is a technique that processes an array incrementally, maintaining only the relevant updates at each step. Instead of processing all queries upfront, we maintain an active set of queries and update nums only when necessary. Here, the difference array helps us track how nums is being modified, while queries provide the updates at specific points.     

#         Difference Array
# So let’s use Difference Array (DA). We have to allocate another array (lets call it DA) which will handle the queries and whose size is one greater than that of given array (Size of (DA array) = Size of (given array) + 1)..

#           Why decrement at r+1 instead of r?
# The difference array technique works by marking the "start" and "end" effects of a range. When we want to apply an effect to a range [l, r]:

# We increment at position l to indicate "start applying the effect here"
# We decrement at position r+1 to indicate "stop applying the effect here"

# This works because when we calculate the prefix sum later, the effect will be applied to all positions from l up to r, but not to position r+1 and beyond.
# If we decremented at position r instead, we would incorrectly remove the effect from position r itself, which should still be covered by the query.

# 3356. Zero Array Transformation II
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

# Example 1:

# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

# Output: 2

# Explanation:

# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
# Example 2:

# Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

# Output: -1

# Explanation:

# For i = 0 (l = 1, r = 3, val = 2):
# Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
# The array will become [4, 1, 0, 0].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
# The array will become [3, 0, 0, 0], which is not a Zero Array.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 5 * 105
# 1 <= queries.length <= 105
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5        

                




        