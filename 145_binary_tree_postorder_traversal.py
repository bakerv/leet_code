# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_values = []

        def evaluate_nodes(root, return_values):
            # evaluate while a valid node exists
            if root != None:
                # check for left branches, append these first
                evaluate_nodes(root.left, return_values)
                # check for right branches, append these next
                evaluate_nodes(root.right, return_values)
                # only append current node value if no branches exist
                return_values.append(root.val)

        evaluate_nodes(root, return_values)

        return return_values
