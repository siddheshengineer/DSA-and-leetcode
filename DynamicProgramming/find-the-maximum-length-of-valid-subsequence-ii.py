class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 2D Map 
        dp = [[0] * k for _ in range(k)]
        res = 0

        for num in nums:
            num %= k

            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
            
        return res        
# 3202. Find the Maximum Length of Valid Subsequence II
