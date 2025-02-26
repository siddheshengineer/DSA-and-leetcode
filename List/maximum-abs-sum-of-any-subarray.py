class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        # Kadane's algorithm

        def kadane(nums: List[int], min_or_max: bool) -> int:
            max_sum = nums[0]
            cur_sum = 0

            for num in nums:
                if min_or_max == 0:
                    cur_sum = min(cur_sum, 0)
                    cur_sum += num
                    max_sum = min(max_sum, cur_sum)
                else:
                    cur_sum = max(cur_sum, 0)
                    cur_sum += num
                    max_sum = max(max_sum, cur_sum)
            
            return max_sum
        
        neg_sum = abs(kadane(nums, 0))
        pos_sum = kadane(nums, 1)

        return max(neg_sum, pos_sum)

# more time efficient method: 
# class Solution:
#     def maxAbsoluteSum(self, nums: List[int]) -> int:
#         s = list(accumulate(nums, initial=0))
#         return max(s) - min(s)

       
        # ## Bruteforce(O(n^2)) of max sum !max absolute sum
        # max_sum = nums[0]

        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i+1, len(nums)):
        #         cur_sum += nums[j]
        #         max_sum = max(max_sum, cur_sum)
        
        # return max_sum

# 1749. Maximum Absolute Sum of Any Subarray
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 

# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# Example 2:

# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104