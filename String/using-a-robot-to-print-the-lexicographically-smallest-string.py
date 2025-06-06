class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_char = [''] * n
        min_char[-1] = s[-1]

        for i in range(n - 2, -1, -1):
            min_char[i] = min(s[i], min_char[i + 1])
        
        # print(min_char)
        t = [] 
        res = []

        for i in range(n):
            t.append(s[i]) 
            
            while t and (i == n -1 or (t[-1] <= min_char[i + 1])):
                res.append(t.pop())
        
        return ''.join(res)

# 2434. Using a Robot to Print the Lexicographically Smallest String
