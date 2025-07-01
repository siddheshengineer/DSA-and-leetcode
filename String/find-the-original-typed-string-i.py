class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1

        # Without dictonary
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]: 
                res += 1      

        # With a dictonary
        # count = collections.defaultdict(int)

        # for i in range(len(word) - 1):
        #     if word[i] == word[i + 1]:
        #         count[word[i]] += 1

        # for val in count.values():
        #     res += (val)

        return res                 

# 3330. Find the Original Typed String I
