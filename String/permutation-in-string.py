from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        count = Counter(s1)
        #print(count)
        R = len(s1)
        L = 0        

        while R <= len(s2):
            per = Counter(s2[L:R])
            #print(per)
            if (per == count):
                return True
            L += 1
            R += 1
        
        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n1 = len(s1)
#         n2 = len(s2)

#         if n1 > n2:
#             return False

#         s1_counts = [0] * 26
#         s2_counts = [0] * 26

#         for i in range(n1):
#             s1_counts[ord(s1[i]) - 97] += 1
#             s2_counts[ord(s2[i]) - 97] += 1

#         if s1_counts == s2_counts:
#             return True

#         for i in range(n1, n2):
#             s2_counts[ord(s2[i]) - 97] += 1
#             s2_counts[ord(s2[i - n1]) - ord("a")] -= 1
#             if s1_counts == s2_counts:
#                 return True

#         return False

# 567. Permutation in String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


