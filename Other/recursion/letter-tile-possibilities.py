from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)  # Count frequency of each letter
        result = 0  # Track number of valid sequences

        # Backtracking follows a depth-first search (DFS) approach, meaning it goes as deep as possible before backtracking.
        def backtrack(path=""):  # Track current sequence
            nonlocal result
            print(f"Current Path: {path} | Available Letters: {dict(count)}")  # Debugging print
            for char in count:  # Try using each letter
                if count[char] > 0:  # Only use available letters
                    result += 1  # Count this sequence as valid
                    count[char] -= 1  # Use this letter
                    print(f"  → Choose '{char}', result={result}")
                    backtrack(path + char)  # Recurse to form longer sequences
                    count[char] += 1  # Undo choice (backtrack)
                    print(f"  ← Backtrack '{char}', revert state: {dict(count)}")

        backtrack()  # Start recursion
        return result


# from collections import Counter

# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         count = Counter(tiles)  # Count frequency of each letter
#         print(count)

#         def backtrack():
#             nonlocal result
#             for char in count:
#                 if count[char] > 0:  # Only use letters that are available
#                     result += 1  # This sequence is valid
#                     count[char] -= 1  # Use this letter
#                     backtrack()  # Recurse to form longer sequences
#                     count[char] += 1  # Undo choice (backtrack)

#         result = 0  # Track number of valid sequences
#         backtrack()
#         return result

# 1079. Letter Tile Possibilities
# Solved
# Medium
# Topics
# Companies
# Hint
# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: tiles = "AAABBC"
# Output: 188
# Example 3:

# Input: tiles = "V"
# Output: 1
 

# Constraints:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.