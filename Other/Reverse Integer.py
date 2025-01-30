class Solution:
    def reverse(self, x: int) -> int:

        max_value = 2**31 -1
        # min_value = -(2**31)

        max_value = int(max_value/10) #divide max value by 10 to avoid overflow
        # print("max: ", max_value)

        if x<10 and x>=0: #return as is for single digits
            return x
        
        isNegative = x<0

        rem = 0
        x = abs(x) #mod of x

        while (x % 10) == 0: #prune leading zeros
            x = int(x/10)

        while x > 0:
            # print(rem)
            if ((rem > max_value) or ((rem==max_value) and ((x%10) > 6))): #check value of rem and if it less than max or , with addition is less then max
                return 0
            rem = (rem*10) + (x % 10)
            x = x//10

        return -rem if isNegative else rem

# 7. Reverse Integer
# Solved
# Medium
# Topics
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1