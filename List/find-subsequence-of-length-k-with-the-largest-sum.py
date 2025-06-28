class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        numWithIndices = [(num, i) for i, num in enumerate(nums)] # To preserver order

        numWithIndices.sort(key=lambda x: -x[0]) # Sort in decending order (-ve) for first value of tuple (x[0])
        # lambda keyword in Python is used to create anonymous functions — functions without a name. lambda function is just a short, inline function. It’s often used when you need a function for a short time, like as an argument to sort(), map(), or filter().

        topK = sorted(numWithIndices[:k], key=lambda x: x[1]) # Take first k elements and sort using their indices (x[1])

        return [num for num, _ in topK]

# 2099. Find Subsequence of Length K With the Largest Sum
