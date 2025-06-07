class Solution:
    def clearStars(self, s: str) -> str:
        char = [[] for _ in range(26)] # Character stack
        arr = list(s)

        for i, c in enumerate(arr):
            if c != '*':
                char[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    if char[j]:          # Found the smallest no. before *
                        arr[char[j].pop()] = '*' # Replace the last index of smallest char with *
                        break
            
        return ''.join(c for c in arr if c != '*')

# 3170. Lexicographically Minimum String After Removing Stars
