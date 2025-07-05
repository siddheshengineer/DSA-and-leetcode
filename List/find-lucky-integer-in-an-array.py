class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        res = [key for key, val in count.items() if key == val]
        return max(res) if res else -1
# 1394. Find Lucky Integer in an Array
