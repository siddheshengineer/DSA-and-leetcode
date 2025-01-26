class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## implementing this as a kSum problem by passing k=4
        ## approch using 2pointer

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:

            # At the start of the kSum function, we will check three conditions:
            # Have we run out of numbers to choose from?
            # Is the smallest number remaining greater than target / k?
            # If so, then any k numbers we choose will be too large.
            # Is the largest number remaining smaller than target / k?
            # If so, then any k numbers we choose will be too small.
            # If any of these conditions is true, there is no need to continue as no combination of the remaining elements can sum to target        
            result = []

            if not nums:
                return result
            
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return result

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
                        result.append([nums[i]] + subset)
            
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            s = set()

            for i in range(len(nums)):
                if len(result) == 0 or result[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        result.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return result    



        nums.sort() #sorting original array
        return kSum(nums, target, 4) #calling ksum function

        