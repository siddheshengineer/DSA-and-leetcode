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
