class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        dom = max(freq, key=freq.get) # get the dominant number
        val = freq[dom] # freq of dominant no.
        if len(nums) == (val * 2 - 1): # if split is not possible exit early
            return -1 
        count, diff_count = 0, 0

        for i in range(len(nums)):
            if nums[i] != dom: # skip if not the dominant number
                diff_count += 1
                continue
            #print(f"i:",i, "nums:", nums[i])
            count += 1
            rem = val - count # remaning freq of dominant number
            rem_len = (len(nums) - 1) - i
            #print(f"count:",count, "diff:",diff_count, "rem: ",rem, "rem_len: ",rem_len)
            if (count > diff_count ) and (rem > (rem_len - rem)): 
                return i

        return -1

# 2780. Minimum Index of a Valid Split
# Solved
# Medium
# Topics
# Companies
# Hint
# An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

# You are given a 0-indexed integer array nums of length n with one dominant element.

# You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

# 0 <= i < n - 1
# nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
# Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

# Return the minimum index of a valid split. If no valid split exists, return -1.

 

# Example 1:

# Input: nums = [1,2,2,2]
# Output: 2
# Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
# In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
# In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
# Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
# It can be shown that index 2 is the minimum index of a valid split. 