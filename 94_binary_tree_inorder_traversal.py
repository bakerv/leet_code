# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_vals = []
        node_stack = []
        current_node = root
        # continue evaluating while valid nodes exist
        while current_node != None or node_stack != []:

            # check each valid node for a left branch
            while current_node != None:
                node_stack.append(current_node)
                current_node = current_node.left

            # if no left branch exists, append the current nodes value to the return list
            # and check for the existance of a right branch
            current_node = node_stack.pop()
            return_vals.append(current_node.val)
            current_node = current_node.right

        return return_vals
    # Taken from the leetcode solution for Iterating using a stack

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            return_values = []

            def evaluate_nodes(root, return_values):
                # determine if a valid node has been located
                if root != None:
                    # check for a left branch
                    evaluate_nodes(root.left, return_values)
                    # append current value when there is not a left branch
                    return_values.append(root.val)
                    # check for a right branch
                    evaluate_nodes(root.right, return_values)

            evaluate_nodes(root, return_values)

            return return_values
        # taken from the leetcode solution for evaluating nodes using recursion