class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                print(nums[i])
                if (nums[-1] > nums[i]) or (nums[0] < nums[-1]):
                    return False 
                    print(nums[i])

        
        return True if count <= 1 else False