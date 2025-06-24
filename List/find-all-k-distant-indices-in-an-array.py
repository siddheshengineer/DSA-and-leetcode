class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        r = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                l = max(r, i - k)
                r = min(n - 1, i + k) + 1
                for j in range(l, r):
                    res.append(j)
        return res

  # 2200. Find All K-Distant Indices in an Array
