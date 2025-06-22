class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        l = len(s)
        i = 0

        while i < l:
            res.append(s[i:i+k]) # String slice
            i += k
            
        while len(res[-1]) < k: # String concatination
            res[-1] += fill

        return res

# 2138. Divide a String Into Groups of Size k
