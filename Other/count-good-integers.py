class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        data = set() # To store the sorted palindromes
        half = (n + 1) // 2 # Efficient way to generate palindromes of n digits, by iterating over 10**n-2 to 10**n-1
        start, end = 10 ** (half - 1), 10 ** half
        #print(start, end)

        for h in range(start, end):
            h = str(h)
            
            if n % 2 == 0: # Even no. of digits
                s = h + h[::-1] # Create palindromes by reversing the digits
            else: # odd no if digits
                s = h + h[:-1][::-1] # Create palindromes by reversing the digits, except last digit
            
            if int(s) % k == 0: # Divisible by k
                data.add("".join(sorted(s))) # add to the set as a string

        #print(data)
        fact = [1] * (n + 1) # create a factorial table for easy lookup
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        res = 0

        for digit in data:
            count = [0] * 10

            for dig in digit: # get the counter of numbers is digit
                count[int(dig)] += 1
            
            permutaions = 0

            for d in range(1, 10):
                if count[d] == 0:
                    continue
                count[d] -= 1 # set the first digit in permutaion
                p = fact[n - 1] # remaning possible permutaions

                for c in count: # for repeating number, decreses the possibel permutaion
                    p = p // fact[c]

                permutaions += p
                count[d] += 1 # reset the first digit
            
            res += permutaions
        
        return res

# hint: https://www.youtube.com/watch?v=fFTCqOtrq80&t=1284s

# 3272. Find the Count of Good Integers
# Solved
# Hard
# Topics
# Companies
# Hint
# You are given two positive integers n and k.

# An integer x is called k-palindromic if:

# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

# Return the count of good integers containing n digits.

# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

# Example 1:

# Input: n = 3, k = 5

# Output: 27

# Explanation:

# Some of the good integers are:

# 551 because it can be rearranged to form 515.
# 525 because it is already k-palindromic.
# Example 2:

# Input: n = 1, k = 4

# Output: 2

# Explanation:

# The two good integers are 4 and 8.

# Example 3:

# Input: n = 5, k = 6

# Output: 2468

 

# Constraints:

# 1 <= n <= 10
1 <= k <= 9
