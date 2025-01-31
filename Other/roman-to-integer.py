class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        i = 1
        prev = s[0]

        for char in s:
            if i < len(s):
                forw = s[i]

            print(f"char: {char}, prev: {prev}, forw: {forw}")

            if (conv[char]<=conv[prev]) and (conv[char]>=conv[forw]):
                print(f"if loop char {conv[char]}")
                result = conv[char] + result
            elif (conv[char]>=conv[prev]):
                print(f"ifelse loop char {conv[char]}, prev {conv[prev]}")
                result = (conv[char] - conv[prev]) + result
            else:
                print(f"ifelse loop char {conv[char]}, forw {conv[forw]}")
                result = (conv[forw] - conv[char]) + result

            print("result: ", result)
            prev = char
            forw = char
            i += 1
            print()
        
        return result
        
    