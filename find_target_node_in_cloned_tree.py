# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# implementing this with DFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        reference = None
        def traverseTree(original, cloned, target):
            # something new I learned, nonlocal keywork to bring in a non local variable
            nonlocal reference
            if original is not None and cloned is not None:
                if cloned.val == target.val:
                    reference = cloned
                    return
                else:
                    # implementing DFS on BOTH tree to traverse from left to right
                    traverseTree(original.left, cloned.left, target)
                    traverseTree(original.right, cloned.right, target)
            else:
                return
        traverseTree(original, cloned, target)
        return reference