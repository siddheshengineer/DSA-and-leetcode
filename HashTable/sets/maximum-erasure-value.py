class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, max_sum, left = 0, 0, 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                res -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            res += nums[right]
            seen.add(nums[right])
            max_sum = max(res, max_sum)

        return max_sum
# 1695. Maximum Erasure Value
