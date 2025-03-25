class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles] # X co-ordiantes
        y = [(r[1], r[3]) for r in rectangles] # Y co-ordiantes

        x.sort()
        y.sort()

        def count_non_overlaping(intervals):
            count, prev = 0, -1

            for start, end in intervals:
                if prev <= start:
                    count += 1
                prev = max(prev, end)
            
            return count
        
        return True if max(count_non_overlaping(x), count_non_overlaping(y)) >= 3 else False

# 3394. Check if Grid can be Cut into Sections
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

# (startx, starty): The bottom-left corner of the rectangle.
# (endx, endy): The top-right corner of the rectangle.
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

# Each of the three resulting sections formed by the cuts contains at least one rectangle.
# Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.