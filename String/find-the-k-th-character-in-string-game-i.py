class Solution:
    def kthCharacter(self, k: int) -> str:
        ## Approch 2 -> Bit Manipulation & Recursion Simulation
        ans = 0

        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
            
        return chr(ord("a") + ans)


        ## Approch 1 -> Create the string
        word = 'a'
        n = len(word)

        while n < k:
            new_word = ''
            for i in range(n):
                new_word += chr(ord(word[i]) + 1)
            word += new_word
            n = len(word)

        return word[k - 1]      
# 3304. Find the K-th Character in String Game I
