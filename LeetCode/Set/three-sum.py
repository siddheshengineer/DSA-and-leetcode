class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        _hash = {}
        result = []

        for index, i in enumerate(nums):
            _hash[i] = index

        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if index_i != index_j:
                    com = i+j
                    com = -com
                    
                if com in _hash:
                    result.append([i, j, _hash[com].value])

                    # for index_k, k in enumerate(nums):
                    #     if (index_j != index_k) and (k == com):     
                    #         # print(i, j , k, com)                       
                    #         if  k in _hash:
                    #             print(i, j , k, com) 
                    #             result.append([i, j, k])
                    #             break

        
        return result


# 15. 3Sum
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105