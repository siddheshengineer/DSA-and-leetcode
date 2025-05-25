class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        count = collections.Counter(words)
        center = False

        for word in count:
            rev = word[::-1]

            ## if the word is like 'gg'
            if word == rev:
                pairs = count[word] // 2
                res += pairs * 4
                count[word] -= pairs * 2
                if count[word] == 1:
                    center = True

            elif rev in count:

                pairs = min(count[word], count[rev])
                res += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs           


        return res if not center else res + 2

# 2131. Longest Palindrome by Concatenating Two Letter Words
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.

 

# Example 1:

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.
# Example 2:

# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
# Example 3:

# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".
