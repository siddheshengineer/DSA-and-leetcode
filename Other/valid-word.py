class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vow, con = False, False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    vow = True
                else:
                    con = True
            elif not c.isdigit():
                return False
            
        return vow and con

# 3136. Valid Word
