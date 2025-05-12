class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = collections.Counter(digits)
        res = []

        for i in range(1, 10):
            if count[i] == 0: 
                continue
            count[i] -= 1

            for j in range(10):
                if count[j] == 0: 
                    continue
                count[j] -= 1

                for k in range(0, 10, 2):
                    if count[k] == 0:
                        continue
                    count[k] -= 1
                    res.append((i * 100) + (j * 10) + k)
                    count[k] += 1

                count[j] += 1
            count[i] += 1

        return res        
# 2094. Finding 3-Digit Even Numbers
