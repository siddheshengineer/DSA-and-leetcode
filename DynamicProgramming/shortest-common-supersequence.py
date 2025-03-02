class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        ## bottom-up solution
        N, M = len(str1), len(str2)

        prev = [str2[j:] for j in range(M)]
        prev.append("")

        for i in reversed(range(N)):

            cur = [""] * M
            cur.append(str1[i:])

            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j+1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + cur[j+1]
                    if len(res1) < len(res2):
                        cur[j] = res1
                    else:
                        cur[j] = res2

            prev = cur

        return cur[0]

        ## shortest time solution:
    # class Solution:
    #   def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    #     n, m = len(str1), len(str2)
    #     memo = [[0]*(m+1) for _ in range(n+1)]

    #     for i in range(n-1, -1, -1):
    #         curr = [0]*(m+1)
    #         for j in range(m-1, -1, -1):
    #             if str1[i] == str2[j]:
    #                 memo[i][j] = memo[i+1][j+1] + 1
    #             else:
    #                 if memo[i+1][j] > memo[i][j+1]:
    #                     memo[i][j] = memo[i+1][j]
    #                 else:
    #                     memo[i][j] = memo[i][j+1]
    #     res = ''
    #     i, j = 0, 0
    #     while i < n and j < m:
    #         if str1[i] == str2[j]:
    #             res += str1[i]
    #             i += 1
    #             j += 1
    #         elif memo[i+1][j]>= memo[i][j+1]:
    #             res += str1[i]
    #             i += 1
    #         else:
    #             res += str2[j]
    #             j += 1
        
    #     if j < m:
    #         res += str2[j:]
    #     if i < n:
    #         res += str1[i:]
        
    #     return res


        # ## backtrack + memoization -> MLE
        # cache = {} # (i,j) -> string

        # def backtrack(i, j):
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     # base case
        #     if i == len(str1): # if we have exausted 1st string, return 2nd remaning str
        #         return str2[j:]
        #     if j == len(str2):  # if we have exausted 2nd string, return 1st remaning str
        #         return str1[i:]
            
        #     # recursive case
        #     if str1[i] == str2[j]:
        #         return str1[i] + backtrack(i + 1, j + 1)
            
        #     res1 = str1[i] + backtrack(i+1, j)
        #     res2 = str2[j] + backtrack(i, j+1)

        #     if len(res1) < len(res2):
        #         cache[(i, j)] = res1
        #         return res1
        #     cache[(i, j)] = res2
        #     return res2

        # return backtrack(0, 0)

# 1092. Shortest Common Supersequence 
# Solved
# Hard
# Topics
# Companies
# Hint
# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

# Example 1:

# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
# Example 2:

# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.

        