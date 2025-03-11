class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        count =  {c:0 for c in 'abc'}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while all(count.values()):
                count[s[l]] -= 1
                l += 1
            
            res += l

        return res

            # while len(count) == 3:
            #     res += (len(s) - r)
            #     count[s[l]] -= 1
            #     if count[s[l]] == 0:
            #         count.pop(s[l])
            #     l += 1
         
    #     return res
    #class Solution:
    # def numberOfSubstrings(self, s):
    #     n = len(s)
    #     arr = [-1, -1, -1]
    #     cnt = 0
    #     for i in range(n):
    #         ch = s[i]
    #         arr[ord(ch) - ord('a')] = i
    #         cnt += 1 + min(arr)
    #     return cnt

# 1358. Number of Substrings Containing All Three Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1
 

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.