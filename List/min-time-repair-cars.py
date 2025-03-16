class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        ## Binary Search using Range ##
        ## Lower bound is 1 min, that's the least possible values given then constraints
        ## Higher bound will be take any one rank and calculate time required to complete the task just using him

        l, r = 1, (max(ranks)*cars*cars)
        # print(l, r)
        res = 0

        while l <= r:
            mid = (l + r)//2
            if self.isValid(mid, ranks, cars):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def isValid(self, time: int, ranks: List[int], cars: int) -> bool:
        
        repaired_cars = 0

        for rank in ranks:
            repaired_cars += int(math.sqrt(time/rank))
        #print(repaired_cars, time)
        return cars <= repaired_cars

# 2594. Minimum Time to Repair Cars
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

# Return the minimum time taken to repair all the cars.

# Note: All the mechanics can repair the cars simultaneously.

 

# Example 1:

# Input: ranks = [4,2,3,1], cars = 10
# Output: 16
# Explanation: 
# - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
# - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
# - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
# - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
# Example 2:

# Input: ranks = [5,1,8], cars = 6
# Output: 16
# Explanation: 
# - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
# - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​