class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        #negative no. can't be palindrome, i.e. -232 != 232-
        #if a no. ends with zero the it's not a palindrome, i.e. 1010 != 0101

        if (x < 0) or (((x % 10) == 0) and (x!=0)):
            return False

        #1
        #more time and space efficient way!!!!!!!!!!!
        #to avoid overflow, reverse till half
        rev = 0
        while x > rev:
            rev = (rev*10) + (x % 10)
            x = int(x/10)

        return (rev == x) or (int(rev/10) == x)

        #2
        #using old method but not time efficient
        # rem = 0
        # y = x
        # while x > 0:
        #     rem = (rem*10) + (x % 10)
        #     x = int(x/10)
        
        # return y==rem


        #3
        # by using string
        # num = str(x)
        # return num == num[::-1]


# 9. Palindrome Number
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?
        

        

        
        