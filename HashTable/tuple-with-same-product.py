class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        _hash = {} #dictonary to store the results
        for i in range(len(nums)-1):
            for l in range(i+1, len(nums)): # Avoid duplicate pairs by starting from i+1
                prod = nums[i] * nums[l]

                if prod not in _hash:  # Store the frequency of each product in the dictionary
                    _hash[prod] = 1
                else:
                    _hash[prod] += 1
        
        # print(_hash)
        count = 0

        for prod in _hash: # Iterate over stored products in the hash map
            freq = _hash[prod]
            if freq > 1:  # Only consider products that appear at least twice
                count += (freq * (freq - 1) // 2) * 8  # Use combination formula and multiply by 8
            
        return count

        # using defaultdict, can save few lines

# 1726. Tuple with Same Product
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# All elements in nums are distinct.