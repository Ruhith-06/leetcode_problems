# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        lst = []
        def solve(root,path):
            if root == None:
                return root
            path += str(root.val)
            if root.left == None and root.right == None:
                lst.append(path)
                return
            path += "->"
            solve(root.left,path)
            solve(root.right,path)

        solve(root,"")
        return lst
        