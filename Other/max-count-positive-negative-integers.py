class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        ## Binary Search ## Time complexity O(log(n))
        pos = False
        if nums[len(nums) // 2] > 0:
            pos = True
        
        i = 0
        neg, zeros = 0, 0

        while i < len(nums) and nums[i] <= 0:
            if nums[i] < 0:
                neg += 1
            elif nums[i] == 0:
                zeros += 1
            i += 1
        
        return ((len(nums)) - (neg + zeros)) if pos else neg

        ## Brute Force ## Time complexity O(n)
        # pos, neg = 0, 0
        # i, n = 0, len(nums)
        # while i < n:
        #     if nums[i] < 0:
        #         neg += 1
        #     elif nums[i] > 0:
        #         pos += 1
        #     i += 1
        
        # return max(pos, neg)

# 2529. Maximum Count of Positive Integer and Negative Integer
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

 

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

# Constraints:

# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.
 

# Follow up: Can you solve the problem in O(log(n)) time complexity?

        