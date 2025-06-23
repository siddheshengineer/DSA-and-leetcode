class Solution:
    # Create Palindrome
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10 # Remove unit place digit
        while x > 0:
            num = (num * 10) + (x % 10)
            x //= 10
        return num


    def checkBaseKPalindrome(self, num: int, base :int) -> bool:
        digit = []
        while num > 0:
            digit.append(num % base)
            num //= base
        return digit == digit[::-1]


    def kMirror(self, k: int, n: int) -> int:
        sum = 0
        length = 1

        while n > 0:
            # Odd palindromes
            i = length
            while n > 0 and i < length * 10:
                p = self.createPalindrome(i, True)
                if self.checkBaseKPalindrome(p, k):
                    sum += p
                    n -= 1                
                i += 1

            # Even palindromes
            i = length
            while n > 0 and i < length * 10:
                p = self.createPalindrome(i, False)
                if self.checkBaseKPalindrome(p, k):
                    sum += p
                    n -= 1                
                i += 1
            length *= 10


        return sum

# 2081. Sum of k-Mirror Numbers
