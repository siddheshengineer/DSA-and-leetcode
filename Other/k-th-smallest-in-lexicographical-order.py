class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ## Prefix Tree

        curr = 1
        k -= 1

        while k > 0:
            step = self._countSteps(n, curr, curr + 1)
            
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        
        return curr

    def _countSteps(self, n, current, nxt_current):
        steps = 0
        while current <= n:
            steps += min( n + 1, nxt_current) - current # Add the no. of integers between prefix1 and prefix2 to steps, cap at n
            current *= 10 # move to next tree level
            nxt_current *= 10

        return steps

# 440. K-th Smallest in Lexicographical Order
