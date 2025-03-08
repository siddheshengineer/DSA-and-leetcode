class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ###### Sliding window ########
        left, right, ops = 0, 0, 0
        min_ops = k

        while right < len(blocks):
            if blocks[right] == 'W':
                ops += 1 # count white blocks

            if right - left +1 > k: # Ensure window size remains `k`
                if blocks[left] == 'W':
                    ops -= 1  # Remove leftmost 'W' when sliding window
                left += 1

            if right - left + 1 == k: # Update min_ops when window reaches size `k`
                min_ops = min(min_ops, ops)
            
            right += 1 # Expand window

        return min_ops

        ##### Brute Force #######
        # left = 0
        # min_ops = len(blocks)

        # while k <= len(blocks):
        #     ops = 0
        #     for i in range(left, k):
        #         print(i)
        #         if blocks[i] == 'W':
        #             ops += 1
        #     min_ops = min(min_ops, ops)
        #     left += 1
        #     k += 1

        # return min_ops

# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.
# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
 

# Constraints:

# n == blocks.length
# 1 <= n <= 100
# blocks[i] is either 'W' or 'B'.
# 1 <= k <= n