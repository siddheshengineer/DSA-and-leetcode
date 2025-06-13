class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if p == 0:
            return 0
            
        n = len(nums)
        nums.sort()

        ## Checking logic
        def checkMaxDiff(diff):
            count = 0 
            index = 0

            while index < n - 1:
                if nums[index + 1] - nums[index] <= diff: 
                    count += 1
                    index += 1
                index += 1
            return count >= p

        ## BS part
        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l + r) // 2

            if checkMaxDiff(mid):
                r = mid
            else:
                l = mid + 1

        return l

  # 2616. Minimize the Maximum Difference of Pairs
