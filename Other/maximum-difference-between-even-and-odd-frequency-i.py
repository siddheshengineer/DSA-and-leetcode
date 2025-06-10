class Solution:
    def maxDifference(self, s: str) -> int:
        count = collections.Counter(s)
        values = (count.values())

        max_even, max_odd = float('inf'), float('-inf')

        for val in (values):
            if val % 2 == 0:
                max_even = min(max_even, val)
            else:
                max_odd = max(max_odd, val)

        return max_odd - max_even

# 3442. Maximum Difference Between Even and Odd Frequency I
