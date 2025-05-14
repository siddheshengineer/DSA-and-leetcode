class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        ## Recurrence (same as below but use of list instead of hashmap reduces unnecessary overhead)
        MOD = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        #print(cnt)
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % MOD
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        return sum(cnt) % MOD


        ## DP with Frequency map -> TLE
        # count = collections.Counter(s)
        # MOD = 10**9 + 7

        # for _ in range(t):
        #     new_counter = collections.Counter() # reset new_counter

        #     for ch in count:
        #         cnt = count[ch]
        #         if ch == 'z':
        #             new_counter['a'] = (new_counter['a'] + cnt) % MOD
        #             new_counter['b'] = (new_counter['b'] + cnt) % MOD
        #         else:
        #             next_char = chr(ord(ch) + 1)
        #             new_counter[next_char] = (new_counter[next_char] + cnt) % MOD
            
        #     count = new_counter # update counter with new values
        
        # return sum(count.values()) % MOD
            
        ## doesn't work with very large t
        
        # MOD = 10**9 + 7
        # result = len(s)
        # count = collections.Counter(s)
        # character = ord('z') - t + 1
        
        # for keys, values in count.items():
        #     if ord(keys) >= character:
        #         #print(keys, values)
        #         result += values % MOD

        # result += iterations % MOD

        # return result
# 3335. Total Characters in String After Transformations I
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.
