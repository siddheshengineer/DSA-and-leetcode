class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = collections.Counter(word)
        freq = [f for f in count.values()]
        min_del = float('inf')

        # for target in range(1, (freq[-1] + 1)): take longer here but might be better in real world
        for i in range(len(freq)):
            target = freq[i]
            delete = 0

            for f in freq:
                if f < target:
                    delete += f # remove all the frequencies
                elif f > target + k:
                    delete += f - (target + k) # reduce to target + k
                
            min_del = min(min_del, delete)

        return min_del

        # The code first counts the frequency of each character in the string. Then, for every possible target frequency from 1 to the maximum frequency, it simulates adjusting all character frequencies to fall within the range [target, target + k]. Characters with frequencies below the target are deleted entirely, and those above target + k are partially deleted down to that limit. The total number of deletions needed for each target is calculated, and the minimum across all targets is returned. This ensures the final string is k-special—where all character frequencies differ by at most k—with the fewest deletions.

# 3085. Minimum Deletions to Make String K-Special
