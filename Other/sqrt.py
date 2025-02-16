class Solution:
    def mySqrt(self, x: int) -> int:

        if (x == 0) or (x == 1):
            return x
        
        left = 1
        right = x
        mid = ((right-left)//2)+left

        while left<=right:
            mid = ((right-left)//2)+left

            if x == (mid*mid):
                return mid
            elif x < (mid*mid):
                right = mid-1
            else:
                left = mid+1
        
        return right

# 69. Sqrt(x)
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.