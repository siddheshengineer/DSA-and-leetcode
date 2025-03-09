class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        l = 0
        N = len(colors) # To traverse Circular array, mod the index by N i.e i % N

        for r in range(1, N + k - 1):
            if colors[r % N] == colors[(r-1) % N]: # Not alternating
                l = r
            
            if r - l + 1 > k: # If windows is more than k, shorten it
                l += 1
            
            if r - l + 1 == k: # Window is of required size i.e k
                count += 1

        return count

# 3208. Alternating Groups II
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.