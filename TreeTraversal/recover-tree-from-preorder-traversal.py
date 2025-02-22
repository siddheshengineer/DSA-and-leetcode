# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        stack = []
        index = 0

        while index < len(traversal):
            # Extract depth
            depth = 0
            while index<len(traversal) and traversal[index] == '-':
                depth += 1
                index += 1

            # Extract value
            val = 0
            while index<len(traversal) and traversal[index].isdigit():
                val = val*10 + int(traversal[index])
                index += 1
            
            node = TreeNode(val) #creating tree node

            if depth == len(stack):  # If depth matches stack size, it's a LEFT child
                if stack:
                    stack[-1].left = node # attach left child
            else: # If depth is LESS than stack size, it's a RIGHT child
                while len(stack) > depth:  # Pop stack to correct depth
                    stack.pop()
                stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]

# Approach using regular expressions
# import re
# class Solution:
#     def recoverFromPreorder(self, S: str) -> TreeNode:
#         dash_map = {}
#         dash_cnt = 0
#         first_num = ""
#         for ch in S:
#             if ch == '-': break
#             first_num += ch
#         dash_map[0] = TreeNode(int(first_num))
#         s = re.findall(r'(-+)(\d+)', S)
#         for dash, num in s:
#             dash_num = len(dash)
#             num = int(num)
#             n = TreeNode(num)
#             fa = dash_map[dash_num - 1]
#             if not fa.left:
#                 fa.left = n
#             elif not fa.right:
#                 fa.right = n
#             dash_map[dash_num] = n
#         return dash_map[0]


# 1028. Recover a Tree From Preorder Traversal
# Solved
# Hard
# Topics
# Companies
# Hint
# We run a preorder depth-first search (DFS) on the root of a binary tree.

# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

# If a node has only one child, that child is guaranteed to be the left child.

# Given the output traversal of this traversal, recover the tree and return its root.

 

# Example 1:


# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# Example 2:


# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# Example 3:


# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
 

# Constraints:

# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 109

