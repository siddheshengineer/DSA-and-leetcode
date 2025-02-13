from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        dig_sum = defaultdict(list)

        for index, num in enumerate(nums): # get sum of each individual element of the list
            digitSum = 0
            while (num > 0):
                digitSum += num % 10
                num //= 10
            dig_sum[digitSum].append(nums[index])

        for item in dig_sum.values():
            if len(item) > 1:    # only consider those elements who have same sum as other element in the list
                if len(item) > 2: # we only need (i,j) sum, so if have more than 2 elements
                    item.sort()   # sort the list

                    while len(item) > 2: # while we have more than 2 elements
                        item.pop(0) # remove first element
                item_sum = sum(item)

                max_sum = max(max_sum,item_sum)

        return max_sum
        
# 2342. Max Sum of a Pair With Equal Sum of Digits
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

# Example 1:

# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.
# Example 2:

# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109