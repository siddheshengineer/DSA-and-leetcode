class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Lograthimic
        return n > 0 and (math.log2(n) % 1 == 0)

        # # Recursion
        # if (n == 1):
        #     return True
        # if n < 1 or n % 2 !=0 :
        #     return False
        # return self.isPowerOfTwo(n // 2)
# 231. Power of Two
  
