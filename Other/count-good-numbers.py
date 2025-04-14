class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # for even index, possibilities is 5 (even no. from 0 - 9)
        # for odd index, possibilities is 4 (prime no. from 0 - 9)
        # for n digit number, no if even and odd index is roughly n/2

        MOD = 10**9 + 7

        def pow(x, n):
            res = 1
            while n > 0:
                if n % 2: #if power is odd, then X(X * X)^n //2
                    res = (res * x) % MOD
                n = n // 2
                x = (x * x) % MOD

            return res    

        even = ceil(n / 2)
        odd = n // 2

        return(pow(5, even) * pow(4, odd)) % MOD

# 1922. Count Good Numbers
# Solved
# Medium
# Topics
# Companies
# Hint
# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# Example 2:

# Input: n = 4
# Output: 400
# Example 3:

# Input: n = 50
# Output: 564908303
