# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(preorder[0])]
        post_index = 0
        for curr in preorder[1:]:
            node = TreeNode(curr)

            while stack[-1].val == postorder[post_index]:
                stack.pop()
                post_index += 1

            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

# 889. Construct Binary Tree from Preorder and Postorder Traversal
# Solved
# Medium
# Topics
# Companies
# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.

 

# Example 1:


# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# Example 2:

# Input: preorder = [1], postorder = [1]
# Output: [1]