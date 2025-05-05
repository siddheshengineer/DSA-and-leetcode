class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10**9 + 7

        if n <= 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5

        for i in range(4, n + 1):
            dp[i] = (2 * dp[i -1] + dp[i - 3]) % MOD
        
        return dp[n]

# 790. Domino and Tromino Tiling
# Solved
# Medium
# Topics
# Companies
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 1000
