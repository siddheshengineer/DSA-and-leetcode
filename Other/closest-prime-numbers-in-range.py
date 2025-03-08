import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def isprime(num: int) -> bool: # Find prime no using traditional method 
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1): # Efficient range to know if the no. is prime or not
                if num % i == 0:  # num is divisble by i, not a prime no
                    return False
            return True

        diff = {}
        last = None

        while left <= right:

            if isprime(left):
                if last is not None:
                    if (left - last) <= 2:  # Return early for closet pair, avoid TLE
                        return [last, left]
                    diff[(last, left)] = left - last  #  Lists are Mutable (Unhashable), meaning their contents can change. Dictionary keys must be immutable (like tuple, int, str).
                last = left
            left += 1

        return min(diff, key=diff.get) if diff else [-1, -1]

    ## Expected solution -> Sieve of Eratosthenes ##
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            """ Generate all prime numbers up to n using Sieve of Eratosthenes """
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

            for i in range(2, int(n ** 0.5) + 1):  # Mark non-primes
                if is_prime[i]:  
                    for j in range(i * i, n + 1, i):  # Mark multiples as non-prime
                        is_prime[j] = False
            return is_prime
        
        # Step 1: Generate primes up to `right`
        is_prime = sieve(right)
        
        # Step 2: Collect primes in range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Step 3: Find the closest prime pair
        if len(primes) < 2:  # If not enough primes, return [-1, -1]
            return [-1, -1]

        min_gap = float('inf')
        best_pair = [-1, -1]

        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                best_pair = [primes[i], primes[i + 1]]

        return best_pair

# 2523. Closest Prime Numbers in Range
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

# Example 1:

# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:

# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

# Constraints:

# 1 <= left <= right <= 106