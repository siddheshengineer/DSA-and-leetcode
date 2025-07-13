class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        res, i, j = 0, 0, 0
        m, n = len(players), len(trainers)

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            
            if j < n:
                res += 1
            i += 1
            j += 1
        
        return res

# 2410. Maximum Matching of Players With Trainers
