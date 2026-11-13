# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root == None:
            return True
        
        def solve(left,right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            return solve(left.left, right.right) and solve(left.right, right.left)

        return solve(root.left, root.right)