class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        ## Using Sliding window
        count, start, mini, maxi = 0, -1, -1, -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i
            if nums[i] == maxK:
                maxi = i
            if nums[i] == minK:
                mini = i
            valid = max(0, min(mini, maxi) - start)
            count += valid
        
        return count

        ## Using Double Deque / Monotonic Queue
        # count = 0
        # left = 0
        # dq_min, dq_max = deque(), deque()

        # for i in range(len(nums)):
        #     if nums[i] < minK or nums[i] > maxK:
        #         dq_min.clear()
        #         dq_max.clear()
        #         left = i + 1
        #         continue
            
        #     while dq_min and nums[dq_min[-1]] >= nums[i]:
        #         dq_min.pop()
        #     dq_min.append(i)

        #     while dq_max and nums[dq_max[-1]] <= nums[i]:
        #         dq_max.pop()
        #     dq_max.append(i)

        #     if nums[dq_min[0]] == minK and nums[dq_max[0]] == maxK:
        #         start = min(dq_min[0], dq_max[0])
        #         count += (start - left + 1)
            
        # return count




        ## Brute Force TLE
        # count = 0

        # for i in range(len(nums)):
        #     mini, maxi = float('inf'), float('-inf')

        #     for j in range(i, len(nums)):

        #         mini = min(mini, nums[j])
        #         maxi = max(maxi, nums[j])

        #         if mini == minK and maxi == maxK:
        #             count += 1
        
        # return count
# 2444. Count Subarrays With Fixed Bounds
# Solved
# Hard
# Topics
# Companies
# Hint
# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:

# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i], minK, maxK <= 106
