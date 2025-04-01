class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        ## Knapsack problem

        ## Bottom-up solution
        N = len(questions)
        cache = [0] * N

        for i in reversed(range(N)):

            points, bp = questions[i]
            prev_index = i + 1 + bp 

            choose = points + (cache[prev_index] if prev_index < N else 0) #choose step
            skip = cache[i + 1] if (i + 1) < N else 0 # skip step

            cache[i] = max(choose, skip)
        
        return cache[0]



        # Backtrack + memoization
        # cache = [0] * len(questions)

        # def backtrack(i):
        #     if i >= len(questions):
        #         return 0
            
        #     if cache[i]: # non zero value
        #         return cache[i]
            
        #     points, bp = questions[i]

        #     cache[i] = max(
        #         backtrack(i + 1), # skip question at i
        #         points + backtrack(i + 1 + bp) # choose question at i
        #     )
            
        #     return cache[i]
        
        # return backtrack(0)

        ## Backtrack, bruteforce solution TLE
        # def backtrack(i):
        #     if i >= len(questions):
        #         return 0
            
        #     points, bp = questions[i]

        #     return max(
        #         backtrack(i + 1), # skip question at i
        #         points + backtrack(i + 1 + bp) # choose question at i
        #     )
        
        # return backtrack(0)

# 2140. Solving Questions With Brainpower
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

# The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

# For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
# If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
# If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
# Return the maximum points you can earn for the exam.

 

# Example 1:

# Input: questions = [[3,2],[4,3],[4,4],[2,5]]
# Output: 5
# Explanation: The maximum points can be earned by solving questions 0 and 3.
# - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
# - Unable to solve questions 1 and 2
# - Solve question 3: Earn 2 points
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
# Example 2:

# Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: 7
# Explanation: The maximum points can be earned by solving questions 1 and 4.
# - Skip question 0
# - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
# - Unable to solve questions 2 and 3
# - Solve question 4: Earn 5 points
# Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.