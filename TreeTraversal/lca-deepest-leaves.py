# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Bottom Up solution O(n), DFS
        def dfs(node):
            if not node:
                return (None, 0)
            
            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height == right_height:
                return node, 1 + left_height
            
            if left_height > right_height:
                return left_node, 1 + left_height
            elif left_height < right_height:
                return right_node, 1 + right_height
            
        node, _ = dfs(root)
        return node

# 1123. Lowest Common Ancestor of Deepest Leaves
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A


        