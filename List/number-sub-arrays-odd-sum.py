class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ## Prefix Sum with Odd-Even Counting
        # Instead of computing the sum of every possible subarray from scratch, we can leverage prefix sums to speed things up. The key insight is that the sum of any subarray can be determined by the difference between two prefix sums.

        prefix_sum = 0
        even_count = 0
        odd_count = 0
        result = 0
        MOD = 1e9 + 7

        for i in range(len(arr)):
            prefix_sum = prefix_sum + arr[i]             
            
            if prefix_sum % 2: #Odd num
                result = (result + 1 + even_count) % MOD
                odd_count += 1
            else: #Even num
                result = (result + odd_count) % MOD 
                even_count += 1
        
        return int(result)

        # ## Dynamic programming
        # MOD = 1e9 + 7
        # n = len(arr)

        # # Convert elements to 0 (even) or 1 (odd)
        # for i in range(n):
        #     arr[i] %= 2

        # # dp_even[i] represents the number of subarrays with an even sum ending
        # # at index i. dp_odd[i] represents the number of subarrays with an odd
        # # sum ending at index i
        # dpeven = [0]*n
        # dpodd = [0]*n

        # if arr[n-1] == 1:
        #     dpodd[n-1] = 1
        # else:
        #     dpeven[n-1] = 1

        # # Traverse the array in reverse
        # for num in range(n-2, -1, -1):
        #     if arr[num] == 1: #Odd number
        #         dpodd[num] = (1+ dpeven[num+1]) % MOD # Odd element contributes to odd subarrays
        #         dpeven[num] = dpodd[num+1] # Even element continues the pattern
        #     else:
        #         dpeven[num] = (1+ dpeven[num+1]) % MOD # even element contributes to even subarrays
        #         dpodd[num] = dpodd[num+1] # odd element continues the pattern
        
        # count = 0
        # for odd_count in dpodd:
        #     count += odd_count
        #     count %= MOD
        
        # return int(count)


        ## Brute force TLE
        # MOD = 1e9 + 7
        # n = len(arr)
        # count = 0

        # # Generate all possible subarrays
        # for start_index in range(n):
        #     current_sum = 0
        #     # Iterate through each subarray starting at start_index
        #     for end_index in range(start_index, n):
        #         current_sum += arr[end_index]
        #         # Check if the sum is odd
        #         if current_sum % 2 != 0:
        #             count += 1

        # return int(count % MOD)


# 1524. Number of Sub-arrays With Odd Sum
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers arr, return the number of subarrays with an odd sum.

# Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
# Example 2:

# Input: arr = [2,4,6]
# Output: 0
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
# Example 3:

# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
 

# Constraints:

# 1 <= arr.length <= 105
# 1 <= arr[i] <= 100