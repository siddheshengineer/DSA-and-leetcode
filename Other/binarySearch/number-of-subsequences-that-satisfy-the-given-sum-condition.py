class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n, MOD = len(nums), 10**9 + 7
        nums.sort()

        power = [1] * n # Pre computing powers, to calculate no. of subsequence
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD


        l, r = 0, n - 1
        res = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + power[r - l]) % MOD
                l += 1
            else:
                r -= 1
            
        return res
# 1498. Number of Subsequences That Satisfy the Given Sum Condition
